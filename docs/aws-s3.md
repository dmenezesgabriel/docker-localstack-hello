# S3 - Simple Storage Service

Aws storages examples:

- S3
- EFS
- Glacier
- Storage Gateway
- Snowball
- Snowmobile
- cloudFront
- RDS
- DynamoDB
- Redshift
- ElastiCache
- Neptune

## Description

- Storage any type of files (5 Terabytes for file)
- Unlimited storage (Charged per Gigabyte)
- Create Buckets (similar to hd partitions) with folders inside.

## Features

- Versioning
- Encryption
- ACL

## Components

Object Base

- Key: File name
- Value: File content
- Version: File version (If enabled)
- Metadata: Tag, local, etc
- ACL

## Tiers

- S3 Standard: Replicated for at least 2 availability zones, with 99.99% of availability and durability.
- S3 IA (Infrequent Access): Cheaper, but with a access fee, replicated for at least 2 availability zones.
- S3 One Zone: Similar with IA but with one availability zone.
- Glacier: For backup purposes, it takes from 3 to 5 hours to retrieve a file.

## Charges

- Storage: Per Gigabyte
- Request: Per Access
- Storage management price (Tags, Versioning)
- DTP (Data Transfer Pricing): Transfer between regions.
- Transfer Acceleration: CDN, CloudFront

## Buckets

- Bucket name must be unique

## Security

- Bucket Policy: Allow access to a bucket from a specific IP
- ACL: Allow access to a bucket from a specific user
- Encryption: Encrypt files in a bucket
- Versioning: Keep versions of files
- MFA Delete: Require MFA to delete a file
- Signed URL: Generate a URL with expiration time to access a file
- CORS: Allow access from another domain

## Storage Classes

- S3 Standard: Replicated for at least 2 availability zones, with 99.99% of availability and durability.
- Intelligent Tiering: Automatically move files between tiers based on access frequency.
- S3 IA (Infrequent Access): Cheaper, but with a access fee, replicated for at least 2 availability zones.
- S3 One Zone: Similar with IA but with one availability zone.
- Glacier: For backup purposes, it takes from 3 to 5 hours to retrieve a file.
- Glacier Insant Retrival: For backup purposes, it takes from 1 to 5 minutes to retrieve a file.
- Glacier Deep Archive: For backup purposes, it takes from 12 to 48 hours to retrieve a file.
- S3 Outposts: For on-premises applications.
