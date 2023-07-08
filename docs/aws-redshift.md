# Redshift

## Description

> Data warehousing as a service.

Redshift is a managed data warehouse service. It is a regional service, so it can be accessed from all AZs in the region.

- Redshift is based on PostgresSQL, but it's not used for OLTP (online transaction processing).
- It's OLAP(online analytical processing) - used for analytics and data warehousing.
- Load data once every hour, not every second.
- Columnar storage of data instead of row based.
- Massive parallel processing (MPP) - parallel processing of data.
