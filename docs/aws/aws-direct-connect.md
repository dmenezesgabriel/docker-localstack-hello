# AWS Direct Connect

## Description

AWS Direct Connect is a cloud service solution that makes it easy to establish a dedicated network connection from your premises to AWS. Using AWS Direct Connect, you can establish private connectivity between AWS and your datacenter, office, or colocation environment, which in many cases can reduce your network costs, increase bandwidth throughput, and provide a more consistent network experience than Internet-based connections.

- _It does not use public internet_

```mermaid
graph TB
    A[Windows Shared Network] -- 1. Establishes Connection --> B(AWS Direct Connect)
    B -- 2. Requests Connection --> C[Direct Connect Location]
    C -- 3. Sets up Physical Connectivity --> D[AWS Direct Connect Router]
    D -- 4. Connects to Amazon S3 --> E[Amazon S3 Bucket]
    E -- 5. Uploads Files --> F[Files Uploaded to Amazon S3]

```
