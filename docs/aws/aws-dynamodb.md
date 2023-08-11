# DynamoDB

## Description

DynamoDB is a serverless NoSQL database service. It is a regional service, so it can be accessed from all AZs in the region.

It stores items, items are composed of attributes. Each attribute has a name and a value. Each item can have a maximum of 400KB of data.

- Each stored item can have different attributes.
- serverless.
- NoSQL database.
- Single digit millisecond latency - low latency retrieval.
- Serverless: no servers to provision, patch, or manage.
- automatic scaling.

### NoSQL

NoSql databases are non-relational databases. They are designed to store and retrieve data in ways that are different from relational databases. They are designed to be highly scalable, and to be able to handle large amounts of data._You cannot link tables, all relevant information must be at one table_.

## Use cases

- Single table no relationship data.
- Employee contact information.
- Product catalog.
- User profile data.

## DynamoDB Accelerator (DAX)

DAX is a fully managed, highly available, in-memory cache for DynamoDB. It improves the performance of DynamoDB queries by dramatically reducing read latency, allowing applications to read data from a fast, in-memory cache in microseconds instead of from DynamoDB in milliseconds.

It is only used with DynamoDB while elasticache can be used for other databases.

## RDS vs DynamoDB

- DynamoDB is a NoSQL database, RDS is a relational database.
- DynamoDB is serverless, RDS is not.
- DynamoDB is a regional service, RDS is a regional service.
- DynamoDB is a key-value and document database, RDS is a relational database.

## Price

- DynamoDB is cheaper than RDS.
- DynamoDB is cheaper than Aurora.
- DynamoDB is cheaper than Redshift.
