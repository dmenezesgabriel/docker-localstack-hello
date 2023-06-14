# DynamoDB

## Description

DynamoDB is a serverless NoSQL database service. It is a regional service, so it can be accessed from all AZs in the region.

It stores items, items are composed of attributes. Each attribute has a name and a value. Each item can have a maximum of 400KB of data.

- Each stored item can have different attributes.
- Millisecond latency at any scale.
- Serveless: no servers to provision, patch, or manage.
- automatic scaling.

## Use cases

- Single table no relationship data.
- Employee contact information.
- Product catalog.
- User profile data.

## RDS vs DynamoDB

- DynamoDB is a NoSQL database, RDS is a relational database.
- DynamoDB is serverless, RDS is not.
- DynamoDB is a regional service, RDS is a regional service.
- DynamoDB is a key-value and document database, RDS is a relational database.

## Price

- DynamoDB is cheaper than RDS.
- DynamoDB is cheaper than Aurora.
- DynamoDB is cheaper than Redshift.
