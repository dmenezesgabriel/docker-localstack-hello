# S3 - Simple Storage Service

## Description

- Storage any type of files (5 Terabytes for file)
- Unlimited storage (Charged per Gigabyte)
- Create Buckets (similar to hd partitions) with folders inside.

## Features

- 9.99999999999% of durability (11 9s)
- 99.99% availability (out of 1 year, 1 hour of downtime)
- Block Public Access
- Versioning
- Encryption
- ACL

### Encryption

### Server Side Encryption

- S3 Managed Keys - SSE-S3
- always encrypted at rest

### Client Side Encryption

- KMS Managed Keys - SSE-KMS

## Buckets

A Bucket is a container for objects stored in Amazon S3. Every object is contained in a bucket. For example, if the object named photos/puppy.jpg is stored in the johnsmith bucket, then it is addressable using the URL http://johnsmith.s3.amazonaws.com/photos/puppy.jpg.

- Each bucket name must be unique across all of Amazon S3.

## Object Storage

Object storage is a storage architecture that manages data as objects, as opposed to other storage architectures like file systems which manage data as a file hierarchy and block storage which manages data as blocks within sectors and tracks.

### Object Structure

- Data: Files
- Metadata: File name, size, etc.
- Key: File name

### Object Storage vs Block Storage

- Object Storage: Store files in buckets, with metadata and a key.
- Block Storage: Store files in blocks, with a file system.

When you modify a file in block storage, only the modified pieces are changed. In object storage, the entire file is replaced.

## Pricing

- **Storage**: You pay only for the storage that you use. You are charged the rate to store objects in your Amazon S3 buckets based on your objects sizes, storage classes, and how long you have stored each object during the month.
- **Request**: and data retrievals: Per You pay for requests made to your Amazon S3 objects and buckets. For example, suppose that you are storing photo files in Amazon S3. You are charged for each GET, LIST, or SELECT request made to Amazon S3. You are also charged for each GB of data scanned by SELECT requests.
- **Data transfer**: There is no cost to transfer data between different Amazon S3 buckets or from Amazon S3 to any service within the same AWS Region. However, you pay for data that you transfer in or out of Amazon S3, with a few exceptions. There is no cost for data transferred into Amazon S3 from the internet or out to Amazon CloudFront. There is also no cost for data transferred out to an Amazon EC2 instance, when the instance is in the same AWS Region as the S3 bucket. Data transferred between Amazon S3 and Amazon Glacier in the same AWS Region is free.
- **Management and replication**: You pay for the storage management features that you have enabled on your account's Amazon S3 buckets,. THese features include Amazon S3 Inventory, Amazon S3 Analytics, and Amazon S3 Object Tagging.

## Security

- Bucket Policy: Allow access to a bucket from a specific IP
- ACL: Allow access to a bucket from a specific user
- Encryption: Encrypt files in a bucket
- Versioning: Keep versions of files
- MFA Delete: Require MFA to delete a file
- Signed URL: Generate a URL with expiration time to access a file
- CORS: Allow access from another domain

## Storage Classes (Tiers)

### S3 Standard

- Ideal for frequently accessed data that needs to be delivered with low latency and high throughput.
- Stores data in a minimum of three Availability Zones (AZs) to protect against the loss of one or two facilities.
- It is a good choice for a wide variety of use cases like cloud applications, dynamic websites, content distribution, mobile and gaming applications, and big data analytics.

### S3 Standard-IA (Infrequent Access)

- Ideal for long-lived, but less frequently accessed data.
- Similar to S3 Standard, but with a lower per GB storage price and a per GB retrieval fee.
- It is a good choice for data that is accessed less frequently, but requires rapid access when needed. For example, backups and disaster recovery data.
- Both S3 Standard and S3 Standard-IA store data in a minimum of three Availability Zones (AZs) to protect against the loss of one or two facilities.

### S3 One Zone-IA

- Ideal for long-lived, but less frequently accessed data that doesn’t require the level of availability and resilience of S3 Standard or S3 Standard-IA.
- Stores data in a single AZ and costs 20% less than S3 Standard-IA.
- It is a good choice for secondary backup copies of on-premises data and for storing data you can recreate.

### S3 Intelligent-Tiering

- Ideal for data with unknown or changing access patterns.
- If you haven't accessed an object for 30 consecutive days, Amazon S3 moves it to the infrequent access tier. If you access an object in the infrequent access tier, Amazon S3 moves it back to the frequent access tier.
- It is a good choice for data with unknown or changing access patterns, such as new data sets or data sets that are rarely accessed. It is also a good choice when you want to save costs on long-lived data sets for which access patterns are unknown or unpredictable.

### S3 Glacier

Enables encryption bu default

#### S3 Glacier Instant Retrieval

- Works well for data that is infrequently accessed, but requires rapid access when needed.

#### S3 Glacier Flexible Retrieval

- Ideal for data that is rarely accessed like archives, which may be needed in minutes or hours.

#### S3 Glacier Deep Archive

- Lowest cost storage class for data archiving. Ideal for long-term retention of data that is accessed once or twice a year.
- Able to retrieve objects within 12 to 48 hours.
- Data that might be accessed in a year or longer.

### S3 Outposts

- Create S3 buckets on-premises.
- Use the same APIs and tools to manage data on-premises and in the cloud.
- is designed to meet the needs of customers who have workloads that require low latency access to on-premises data and local data processing.

## Management Tools

### Storage Class Analysis

- Analyze the access frequency of files and suggest the best storage class for each file.

### S3 Lifecycle Policy

- Move files between tiers based on access frequency.

Example: Move files to IA after 30 days, and to Glacier after 60 days.

### Replication flavors

#### Cross Region Replication

- Replicate files to another region.

#### Same Region Replication

- Replicate files to another bucket in the same region.

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

## EBS vs S3

- Ocasional changes: S3
- Backup: S3
- Complex editing and high IO: EBS
