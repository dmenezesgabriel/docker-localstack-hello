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
