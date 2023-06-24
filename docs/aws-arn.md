# Amazon Resource Names (ARNs)

## Description

Amazon Resource Names (ARNs) uniquely identify AWS resources. We use ARNs to identify resources in AWS CloudFormation templates, and to manage permissions in AWS Identity and Access Management (IAM).

`arn:partition:service:region:account-id:resource`

- **partition**: The partition that the resource is in. For standard AWS regions, the partition is aws. If you have resources in other partitions, the partition is aws-partitionname. For example, the partition for resources in the China (Beijing) region is aws-cn.
- **service**: The service namespace that identifies the AWS product (for example, Amazon S3, IAM, or Amazon RDS). For a list of namespaces, see [AWS Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces) in the _AWS General Reference_.
- **region**: The region where the resource is located. For a list of regions, see [AWS Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html) in the _AWS General Reference_. For resources that are not regional, such as IAM, use us-east-1. This placeholder value permits the ARN to be parsed without knowing the resource location in advance. Note that the ARNs for some resources do not require a region, so this component might be omitted.
- **account-id**: The ID of the AWS account that owns the resource, without the hyphens. For example, 123456789012. Note that the ARNs for some resources don't require an account number, so this component might be omitted.
- **resource**: The content of this part of the ARN varies by service. It often includes an indicator of the type of resource—for example, an IAM user or Amazon RDS database —followed by a slash (/) or a colon (:), followed by the resource name itself. Some resources might require more than one additional identifier. For example, an Amazon S3 bucket has a resource name that includes the bucket name and AWS Region name. For more information, see [Resource Types](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces) in the _AWS General Reference_.

Example:

Amazon S3 does not require region or account-id parameters in ARNs, so those sections are left blank. However, the “:” to separate the sections is still used, so it looks similar to arn:aws:s3:::reportbucket987987
