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

### SQS

- **Create an SQS queue named test-queue**:

  ```sh
  awslocal sqs create-queue --queue-name test-queue
  # Output:
  # {
  #    "QueueUrl": "http://localhost:4566/000000000000/test-queue"
  # }
  ```

- **Send a message to the SQS created above**:

  ```sh
  awslocal sqs send-message --queue-url http://localhost:4566/000000000000/test-queue --message-body "test message." --delay-seconds 0
  # Output:
  # {
  #     "MD5OfMessageBody": "5cbd04aaf0430ff7fac38ebd11b72083",
  #     "MessageId": "3a110fce-513c-b6f2-6059-05e145fe60db"
  # }
  ```

- **Receive the sent message from the SQS**:

  ```sh
  awslocal sqs receive-message --queue-url http://localhost:4566/000000000000/test-queue --attribute-names All --message-attribute-names All
  # Output:
  # {
  #     "Messages": [
  #         {
  #             "MessageId": "3a110fce-513c-b6f2-6059-05e145fe60db",
  #             "ReceiptHandle": "uzbggdbobhtkovufriitjvjvrhfdemzqsgluxmohpuxjudarizabcmihywrvvfmmywamuogkhflgbtcpmlesijjeqviorfjwkooppbzqokazqkxhzciqbeiwvvtqqjamoxjmxuviwstjfuoqxafpdntlakygqkefzssemqzbvvkmlinznphlvoepn",
  #             "MD5OfBody": "5cbd04aaf0430ff7fac38ebd11b72083",
  #             "Body": "test message.",
  #             "Attributes": {
  #                 "SenderId": "AIDAIT2UOQQY3AUEKVGXU",
  #                 "SentTimestamp": "1648234565152",
  #                 "ApproximateReceiveCount": "1",
  #                 "ApproximateFirstReceiveTimestamp": "1648234611377"
  #             }
  #         }
  #     ]
  # }
  ```

### Lambda

- **Create a lambda function named test-function**:

  ```sh
  awslocal lambda create-function --function-name test-function --runtime python3.7 --zip-file fileb://test.zip --handler test.lambda_handler --role test
  ```

### API Gateway

- **Create the api gateway called test-api**:

  ```sh
  awslocal apigateway create-rest-api --name test-api
  # Output:
  # {
  #     "id": "br4h590g45",
  #     "name": "test-api",
  #     "createdDate": 1648235267,
  #     "version": "V1",
  #     "binaryMediaTypes": [],
  #     "apiKeySource": "HEADER",
  #     "endpointConfiguration": {
  #         "types": [
  #             "EDGE"
  #         ]
  #     },
  #     "tags": {},
  #     "disableExecuteApiEndpoint": false
  # }
  ```

### Secrets manager

- **Create a secret named localstack-secret in secrets manager**:

  ```sh
  awslocal --endpoint=http://localhost:4566 secretsmanager create-secret \
    --name test-secret \
     --description "This is secret" \
     --secret-string "Some secret" \
     --region=us-east-1
  # Output:
  # {
  #     "ARN": "arn:aws:secretsmanager:us-east-1:000000000000:secret:test-secret-d55114",
  #     "Name": "test-secret",
  #     "VersionId": "0072b882-3871-48e1-a40a-072ff354dcf5"
  # }
  ```

- **Get secret**:

```
awslocal --endpoint=http://localhost:4566 secretsmanager get-secret-value \
  --secret-id test-secret
```

## References

- [ciaranevans](https://github.com/ciaranevans/aws-guild-localstack)
- [kdnuggets](https://www.kdnuggets.com/2021/08/development-testing-etl-pipelines-aws-locally.html)
- [AWS](https://aws.amazon.com/pt/blogs/big-data/developing-aws-glue-etl-jobs-locally-using-a-container/)
- [learnbatta](https://learnbatta.com/blog/aws-localstack-with-docker-compose/)
- [geekhunter](https://blog.geekhunter.com.br/aws-lambda-python-pycharm-localstack/)
- [manomano](https://medium.com/manomano-tech/using-serverless-framework-localstack-to-test-your-aws-applications-locally-17748ffe6755)
- [thomsdacosta](https://thomsdacosta.medium.com/localstack-ambiente-local-para-testar-a-sua-aplica%C3%A7%C3%A3o-aws-4bc255e3ab56)
