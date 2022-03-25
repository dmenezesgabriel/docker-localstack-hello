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

## References

- [ciaranevans](https://github.com/ciaranevans/aws-guild-localstack)
- [kdnuggets](https://www.kdnuggets.com/2021/08/development-testing-etl-pipelines-aws-locally.html)
- [AWS](https://aws.amazon.com/pt/blogs/big-data/developing-aws-glue-etl-jobs-locally-using-a-container/)
