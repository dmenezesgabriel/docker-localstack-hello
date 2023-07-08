# AWS DocumentDB

## Description

> Fast, scalable, highly available, and fully managed document database service that supports MongoDB workloads.

- Aurora is an "AWS Implementation" of MySQL and PostgreSQL, while DocumentDB is an "AWS Implementation" of MongoDB.
- NoSQL database service designed to be compatible with existing MongoDB applications and tools.
- Similar deployment concepts to Aurora.
- Fully managed, highly available, and scalable.
- DocumentDB storage automatically grows in increments of 10 GB, up to 64 TB.
- Automatically scales to workloads with millions of requests per second, thousands of reads and writes per second, and supports up to 15 read replicas.

## Key value database vs document database

- Key value database: data is stored as a key and a value, with no structure.
- Document database: data is stored as a key and a value, but the value is a document, which is a structured object with a schema.
- Document databases are more flexible than key value databases, but less flexible than relational databases.
- Document databases are a good fit for hierarchical data with a lot of one-to-many relationships, such as blog posts and comments.
