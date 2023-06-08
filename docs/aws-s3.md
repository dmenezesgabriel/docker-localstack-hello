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

- 9.99999999999% of durability (11 9s)
- Block Public Access
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
- S3 Intelligent Tiering: Automatically move files between tiers based on access frequency.
- S3 Standard IA (Infrequently Accessed data): Cheaper, but with a access fee, replicated for at least 2 availability zones.
- S3 One Zone IA (Infrequently Accessed data): Similar with IA but with one availability zone.
- S3 Glacier Instant Retrieval: For backup purposes, it takes from 1 to 5 minutes to retrieve a file.
- S3 Glacier Flexible Retrieval: For backup purposes, it takes from 5 to 12 hours to retrieve a file.
- S3 Glacier Deep Archive: For backup purposes, it takes from 12 to 48 hours to retrieve a file.

### Glacier

#### Retrieval Options of Glacier

- Expedited: 1 to 5 minutes
- Standard: 3 to 5 hours
- Bulk: 5 to 12 hours

### Glacier Deep Archive

#### Retrieval Options of Deep Archive

- Standard: 12 hours
- Bulk: 48 hours

## Management Tools

### Storage Class Analysis

- Analyze the access frequency of files and suggest the best storage class for each file.

### S3 Lifecycle Policy

- Move files between tiers based on access frequency.

### S3 Cross Region Replication

- Replicate files between regions.

### S3 Object Lock

- Prevent files from being deleted or modified for a specified period of time.
- WORM (Write Once Read Many)

### S3 Inventory

- List all objects (files) in a bucket, with metadata and encryption status.

### S3 Batch Operations

- Run tasks in batches, such as copying files between buckets, changing storage class, etc.

## Query-in-place services for analytics

- S3 Select: Retrieve only a part of a file.
- Glacier Select: Retrieve only a part of a file.
- Athena: Query data in S3.
- Redshift Spectrum: Query data in S3.

## Versioning

- Keep versions of files.

## Access Management

- Private by default.

### Resource Based Policies

- Bucket Policy: Written in JSON, can be attached to IAM users, groups or roles.
- Access Control List (ACL): Legacy mode, not recommended.
- Query string authentication

### User Based Policies

- IAM Policies
