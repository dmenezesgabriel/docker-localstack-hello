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

s3_resource = boto3.resource(
    "s3",
    region_name=AWS_REGION,
    endpoint_url=ENDPOINT_URL,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)


def list_buckets():
    """
    List s3 buckets
    """
    try:
        response = s3_resource.buckets.all()
    except Exception as error:
        logger.exception(error)
        raise
    else:
        return response


if __name__ == "__main__":
    buckets_list = list_buckets()
    print("Buckets: ")
    for bucket in buckets_list:
        print(bucket.name)
