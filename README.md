# localstack-sdx

## Requirements

- Docker
- Docker Compose
- Python 3

## Setup

### AWS Local CLI

[Github](https://github.com/localstack/awscli-local)

**Create a Python virtual environment**:

```sh
python -m venv venv
```

**Activate environment**:

On windows

```sh
source venv/Scripts/activate
```

On Linux

```sh
source venv/bin/activate
```

**Install deps**:

```sh
pip install -r requirements.txt
```

## Usage

**Run Localstack**:

```sh
docker-compose up localstack
```

- **Check Services Health**:
  http://localhost:4566/health

- **In docker shell command**:

  ```sh
  awslocal --endpoint-url=http://host.docker.internal:4566 s3 ls
  ```

- **In docker's host shell command**:
  ```sh
  awslocal --endpoint-url=http://localhost:4566 s3 ls
  ```

### S3

- **Create a S3 Bucket**:

  ```sh
  awslocal --endpoint-url=http://localhost:4566 s3 mb s3://user-uploads
  # Output: make_bucket: user-uploads
  ```

- **Confirm that Bucket exists**:

  ```sh
  awslocal --endpoint-url=http://localhost:4566 s3 ls
  # Output: 2022-03-25 13:36:46 user-uploads
  ```

- **Create folder**:

  ```sh
  awslocal --endpoint-url=http://localhost:4566 s3api put-object --bucket user-uploads --key lambda
  # Output:
  # {
  #    "ETag": "\"d41d8cd98f00b204e9800998ecf8427e\""
  # }
  ```

- **List Buckets**:

  ```sh
  awslocal --endpoint-url=http://localhost:4566 s3api list-buckets
  ```

- **Copy files to bucket**:
  ```sh
  awslocal --endpoint-url=http://localhost:4566 s3 cp ./samples/lambda/ s3://user-uploads/lambda/ --recursive
  ```

### API Gateway

- **Create the api gateway called test-api**:

  ```sh
  awslocal apigateway create-rest-api --name test-api
  ```

### Lambda

- **Create a lambda function named test-function**:

  ```sh
  awslocal lambda create-function --function-name test-function --runtime python3.7 --zip-file fileb://test.zip --handler test.lambda_handler --role test
  ```

### SQS

- **Create an SQS queue named test-queue**:

  ```sh
  awslocal sqs create-queue --queue-name test-queue
  ```

- **Send a message to the SQS created above**:

  ```sh
  awslocal sqs send-message --queue-url http://localhost:4566/000000000000/test-queue --message-body "test message." --delay-seconds 0
  ```

- **Receive the sent message from the SQS**:

  ```sh
  awslocal sqs receive-message --queue-url http://localhost:4566/000000000000/test-queue --attribute-names All --message-attribute-names All
  ```

### Secrets manager

- **Create a secret named localstack-secret in secrets manager**:
  ```sh
  awslocal secretsmanager create-secret --name localstack-secret
  ```

## References

- [ciaranevans](https://github.com/ciaranevans/aws-guild-localstack)
- [kdnuggets](https://www.kdnuggets.com/2021/08/development-testing-etl-pipelines-aws-locally.html)
- [AWS](https://aws.amazon.com/pt/blogs/big-data/developing-aws-glue-etl-jobs-locally-using-a-container/)
- [learnbatta](https://learnbatta.com/blog/aws-localstack-with-docker-compose/)
- [geekhunter](https://blog.geekhunter.com.br/aws-lambda-python-pycharm-localstack/)
