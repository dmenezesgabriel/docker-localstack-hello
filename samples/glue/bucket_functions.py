import os

import boto3
from pyspark.sql import SparkSession


def add_to_bucket(bucket_name: str, file_name: str) -> None:
    """
    Add file to bucket.
    """
    try:
        # Docker can access it's hosting machine point to
        # host.docker.internal
        s3 = boto3.client(
            "s3",
            endpoint_url="http://host.docker.internal:4566",
            use_ssl=False,
            aws_access_key_id="mock",
            aws_secret_access_key="mock",
            region_name="us-east-1",
        )
        s3.create_bucket(Bucket=bucket_name)

        file_key = f"{os.getcwd()}/{file_name}"
        with open(file_key, "rb") as f:
            s3.put_object(Body=f, Bucket=bucket_name, Key=file_name)
        print(file_name)

        return s3
    except Exception as e:
        print(e)
        return None


def create_testing_pyspark_session():
    print("creating pyspark session")
    spark_session = (
        SparkSession.builder.master("local[2]")
        .appName("pyspark-demo")
        .enableHiveSupport()
        .getOrCreate()
    )

    hadoop_configuration = (
        spark_session.sparkContext._jsc.hadoopConfiguration()
    )
    hadoop_configuration.set(
        "fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem"
    )
    hadoop_configuration.set("fs.s3a.path.style.access", "true")
    hadoop_configuration.set("fs.s3a.connection.ssl.enabled", "false")
    hadoop_configuration.set("com.amazonaws.services.s3a.enableV4", "true")
    hadoop_configuration.set(
        "fs.s3a.aws.credentials.provider",
        "org.apache.hadoop.fs.s3a.TemporaryAWSCredentialsProvider",
    )
    hadoop_configuration.set("fs.s3a.access.key", "mock")
    hadoop_configuration.set("fs.s3a.secret.key", "mock")
    hadoop_configuration.set("fs.s3a.session.token", "mock")
    hadoop_configuration.set(
        "fs.s3a.endpoint", "http://host.docker.internal:4566"
    )
    return spark_session


test_bucket = "user-uploads"
# Write to S3 bucket
add_to_bucket(bucket_name=test_bucket, file_name="dummy.csv")
spark_session = create_testing_pyspark_session()

# Read from s3 bucket
file_path = f"s3a://{test_bucket}/dummy.csv"
data_df = (
    spark_session.read.option("delimiter", ",")
    .option("header", "true")
    .option("inferSchema", "False")
    .format("csv")
    .load(file_path)
)
print(data_df.show())

# Write to S3 as parquet
write_path = f"s3a://{test_bucket}/testparquet/"
data_df.write.parquet(write_path, mode="overwrite")
