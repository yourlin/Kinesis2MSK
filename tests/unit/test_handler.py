import json

import pytest

from kinesis_to_msk import app


@pytest.fixture()
def kinesis_event():
    """ Generates kinesis Event"""

    return {
        "Records": [
            {
                "kinesis": {
                    "kinesisSchemaVersion": "1.0",
                    "partitionKey": "1",
                    "sequenceNumber": "49590338271490256608559692538361571095921575989136588898",
                    "data": "eyJudW0iOiAxMDAwMCwgInRzIjogIjIwMjItMTItMjEgMTI6NDY6MzYifQ==",
                    "approximateArrivalTimestamp": 1545084650.987
                },
                "eventSource": "aws:kinesis",
                "eventVersion": "1.0",
                "eventID": "shardId-000000000006:49590338271490256608559692538361571095921575989136588898",
                "eventName": "aws:kinesis:record",
                "invokeIdentityArn": "arn:aws:iam::123456789012:role/lambda-role",
                "awsRegion": "us-east-2",
                "eventSourceARN": "arn:aws:kinesis:us-east-2:123456789012:stream/lambda-stream"
            },
            {
                "kinesis": {
                    "kinesisSchemaVersion": "1.0",
                    "partitionKey": "1",
                    "sequenceNumber": "49590338271490256608559692540925702759324208523137515618",
                    "data": "eyJudW0iOiAxMDAwMCwgInRzIjogIjIwMjItMTItMjEgMTI6NDY6MzYifQ==",
                    "approximateArrivalTimestamp": 1545084711.166
                },
                "eventSource": "aws:kinesis",
                "eventVersion": "1.0",
                "eventID": "shardId-000000000006:49590338271490256608559692540925702759324208523137515618",
                "eventName": "aws:kinesis:record",
                "invokeIdentityArn": "arn:aws:iam::123456789012:role/lambda-role",
                "awsRegion": "us-east-2",
                "eventSourceARN": "arn:aws:kinesis:us-east-2:123456789012:stream/lambda-stream"
            }
        ]
    }


def test_lambda_handler(kinesis_event):
    ret = app.lambda_handler(kinesis_event, "")
    data = json.loads(ret["Records"])

    for item in data:
        assert "kinesis" in item
