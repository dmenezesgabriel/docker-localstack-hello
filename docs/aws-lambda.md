# AWS Lambda

## Description

AWS Lambda is a serverless compute service that runs your code in response to events and automatically manages the underlying compute resources for you. You can use AWS Lambda to extend other AWS services with custom logic, or create your own back-end services that operate at AWS scale, performance, and security.

- Event-driven compute service: functions get invoked by AWS when needed

## Usage examples

- Serverless cron jobs: CloudWatch Events Event Bridge can trigger Lambda functions periodically

## Triggering Lambda Functions

### API Gateway

API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale. You can create an API that acts as a "front door" for applications to access data, business logic, or functionality from your back-end services, such as workloads running on Amazon Elastic Compute Cloud (Amazon EC2), code running on AWS Lambda, or any web application.

## Pricing

AWS Lambda pricing is based on the number of **requests** for your functions and the **duration**, the time it takes for your code to execute. The AWS Lambda free usage tier includes 1M free requests per month and 400,000 GB of compute time per month. For more information, see [AWS Lambda Pricing](https://aws.amazon.com/lambda/pricing/).

You can save on AWS Lambda costs by signing up for Compute Saving Plans. A compute Savings Plan offers lower compute costs in exchange for committing to a consistent amount of usage over a 1-year or 3-year term. This is an example of paying less when you reserve. For more information, see [AWS Compute Savings Plans](https://aws.amazon.com/savingsplans/compute/).

In summary:

- By the time run x by the ram provisioned
- By the number of invocations
