# Amazon Resource Names (ARNs)

## Description

Amazon Resource Names (ARNs) uniquely identify AWS resources. We use ARNs to identify resources in AWS CloudFormation templates, and to manage permissions in AWS Identity and Access Management (IAM).

`arn:partition:service:region:account-id:resource`

Example:

Amazon S3 does not require region or account-id parameters in ARNs, so those sections are left blank. However, the “:” to separate the sections is still used, so it looks similar to arn:aws:s3:::reportbucket987987
