# AWS Batch

## Description

A batch job is a job with a start and an end, batch will dynamically launch EC2 instances or Sport instances to run the job and terminate them when the job is done.
batch jobs are defined as Docker images and run on ECS.

## AWS Batch vs AWS Lambda

- Lambda has a time limit of 15 minutes, Batch has no time limit.
- Lambda has limited runtime options, Batch can run any Docker image.
- Lambda is event-driven, Batch is not.
- Lambda is serverless, Batch is not.
- lambda has limited temporary disk space, Batch rely on EBS volumes.
