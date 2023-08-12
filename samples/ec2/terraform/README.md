# Terraform AWS EC2 Sample

## Requirements

- [Terraform](https://developer.hashicorp.com/terraform/downloads)
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
- [awscli-local](https://github.com/localstack/awscli-local)

## Setup

```sh
docker run -d -p 4566:4566 -e SERVICES=ec2 localstack/localstack

```

```sh
pip install awscli-local
aws configure set aws_access_key_id test
aws configure set aws_secret_access_key test
aws configure set default.region us-east-1
aws configure set default.output json
aws configure set default.endpoint_url http://localhost:4566
```

## Execution

```sh
terraform init
terraform apply
```

```sh
awslocal ec2 describe-instances
```
