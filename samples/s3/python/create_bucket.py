import json
import logging

import boto3

AWS_REGION = "us-east-1"
AWS_PROFILE = "localstack"
AWS_ACCESS_KEY_ID = "test"
AWS_SECRET_ACCESS_KEY = "test"
ENDPOINT_URL = "http://localhost:4566"

DEFAULT_LOG_FORMAT = (
    "[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d]"
    " %(message)s"
)

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO, format=DEFAULT_LOG_FORMAT)

boto3.setup_default_session(
    profile_name=AWS_PROFILE,
)
s3_client = boto3.client(
    "s3",
    region_name=AWS_REGION,
    endpoint_url=ENDPOINT_URL,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)


def create_bucket(bucket_name: str) -> dict | None:
    """
    Creates a S3 Bucket
    """
    return s3_client.create_bucket(Bucket=bucket_name)


if __name__ == "__main__":
    bucket_name = "create-bucket-sample"
    logger.info("Creating S3 bucket locally using LocalStack...")
    bucket_creation_response = create_bucket(bucket_name)
    logger.info(json.dumps(bucket_creation_response, indent=4) + "\n")
