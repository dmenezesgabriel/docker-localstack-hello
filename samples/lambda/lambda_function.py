import json
import urllib.parse

import boto3

HOST = "http://[YOUR_IP]"
# Get the service resource
# To production it's not necessary inform the "endpoint_url" and "region_name"
s3 = boto3.client("s3", endpoint_url=HOST + ":4572", region_name="us-east-1")
sqs = boto3.client("sqs", endpoint_url=HOST + ":4576", region_name="us-east-1")


def lambda_handler(event, context):
    # print("Received event: " + json.dumps(event, indent=2))
    # Get the object from the event and show its content type
    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    key = urllib.parse.unquote_plus(
        event["Records"][0]["s3"]["object"]["key"], encoding="utf-8"
    )
    url_queue = HOST + ":4566/queue/test-queue"
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        deb = {
            "request_id": response["ResponseMetadata"]["RequestId"],
            "queue_url": url_queue,
            "key": key,
            "bucket": bucket,
            "message": "aws lambda with localstack...",
        }
        print("# ======================================================= #")
        print("Send Message")
        # Send message to SQS queue
        response = sqs.send_message(
            QueueUrl=deb["queue_url"], MessageBody=json.dumps(deb)
        )
        print("response: {}".format(response))

        print("# ======================================================= #")
        print("Receive 10 Messages From SQS Queue")
        response = sqs.receive_message(
            QueueUrl=deb["queue_url"],
            MaxNumberOfMessages=10,
            VisibilityTimeout=0,
            WaitTimeSeconds=0,
        )

        print("# ======================================================= #")
        print("Read All Messages From Response")
        messages = response["Messages"]
        for message in messages:
            print("Message: {}".format(message))

        print("Final Output: {}".format(json.dumps(response)))
        return json.dumps(response)

    except Exception as e:
        print(e)
        raise e
