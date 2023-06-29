# IAM

## Description

IAM is the AWS Identity and Access Management service. It is used to manage users, groups, roles, and policies.

## Root user

The root user is the first user created when an AWS account is created. It has full access to all AWS services and resources in the account. It is recommended to not use the root user for day-to-day tasks, but instead to create an IAM user with the appropriate permissions.

## Users

Users are the entities that interact with AWS services and resources. They can be created and managed in the IAM console. Users can be assigned to groups and roles, and can have policies attached to them.

## Groups

Groups are collections of users. They can be created and managed in the IAM console. Groups can have policies attached to them.

## Roles

Roles are used to grant permissions to entities that are not users like AWS services and resources. They can be created and managed in the IAM console. Roles can have policies attached to them.

## Policies

Policy documents are JSON documents that define permissions. They can be attached to users, groups, and roles. Policies can be created and managed in the IAM console.

- **Version**: the version of the policy language (eg 2012-10-17).
- **Statement**: a list of policy statements.
- **Sid**: an optional identifier for the policy statement.
- **Effect**: says whether to Allow or Deny the permissions.
- **Action**: specifies the API calls that can be made against an AWS Service (eg cloudwatch:ListMetrics).
- **Resource**: defines the scope of entities covered by the policy rule (eg a specific Amazon S3 bucket or Amazon EC2 instance, or \* which means any resource).

Example:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Stmt1234567890",
      "Effect": "Allow",
      "Action": ["cloudwatch:ListMetrics"],
      "Resource": "*"
    }
  ]
}
```

**inline policies** are policies that are embedded directly into a user, group, or role.
