# AWS Container Services

## ECS (Elastic Container Service)

Amazon ECS is a highly scalable, fast container management service that makes it easy to run, stop, and manage containers on a cluster.

### EC2 managed

- EC2 Container Service
- You must provision and maintain the underlying EC2 instances that run your containers.
- AWS takes care of starting and stopping containers on the instances, and maintaining the cluster of instances.
- Has integration with ELB, EBS, IAM, CloudWatch, CloudFormation, etc.

## Fargate

- Serverless
- You don't need to provision and maintain the underlying EC2 instances that run your containers.
- AWS just runs containers for you based on the CPU, memory, and networking resources you choose.

## Elastic Container Registry (ECR)

It is a private Docker registry on AWS and s supports private container images. It does not manage the containers, only the images.
