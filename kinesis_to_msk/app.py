import json
import config
import base64

from kafka import KafkaProducer


def lambda_handler(event, context):
    producer = KafkaProducer(bootstrap_servers=config.SERVER,
                             value_serializer=lambda m: json.dumps(m).encode())
    for record in event['Records']:
        payload = base64.b64decode(record["kinesis"]["data"])
        producer.send(config.TOPIC, json.loads(payload))
