# AWS RDS (Relational Database Service)

**RDBMS**: Relational Database Management System.

## Description

RDS is a managed database service for relational databases. It is a regional service, so it can be accessed from all AZs in the region.

- Automated provisioning, OS patching, backups, monitoring, scaling, failover, redundancy.

**Lift and shift**: migrating an application to the cloud without making any changes to the application._RDS cannot be acessed by SSH_

## Price

- 1/10th the cost of commercial databases.

## Amazon Aurora

Aurora is a MySQL and PostgreSQL-compatible relational database built for the cloud. It is a regional service, so it can be accessed from all AZs in the region.

- serverless.
- Continuous backup to S3.
- point in time recovery.
- it replicates 6 copies of data across 3 AZs.
- up to 5x performance improvement over MySQL.
- up to 3x performance improvement over PostgreSQL.
- it costs 20% more than RDS, but is more efficient so you can save money.
