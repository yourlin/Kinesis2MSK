import json
import config
import base64

from kafka import KafkaProducer


def lambda_handler(event, context):
    producer = KafkaProducer(bootstrap_servers=config.SERVER,
                             value_serializer=lambda m: json.dumps(m).encode())
    for record in event['Records']:
        payload = base64.b64decode(record["kinesis"]["data"])

        user_data = json.loads(payload)

        is_custom_topic = False
        if 'attributes' in user_data:
            if 'customer_context' in user_data['attributes']:
                if 'topic_name' in user_data['attributes']['customer_context']:
                    try:
                        print('topic is [' + user_data['attributes']['customer_context']['topic_name'] + ']')
                        producer.send(user_data['attributes']['customer_context']['topic_name'], user_data)
                        is_custom_topic = True
                    except Exception as e:
                        print(e)

        if not is_custom_topic:
            print('no topic found')
