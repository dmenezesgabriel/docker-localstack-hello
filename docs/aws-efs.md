# EFS (Elastic File System)

## Description

EFS is a file storage service for EC2 instances. It is a network file system that can be mounted on multiple EC2 instances at the same time. It is a regional service, so it can be accessed from all AZs in the region. _similar to a shared drive on a network_.

- Works like a shared drive for EC2 instances.
- Stores data across multiple AZs in a region.
- on-premises servers can access EFS using Direct Connect or VPN.

## EBS vs EFS

EBS is a block storage service, while EFS is a file storage service. EBS can only be mounted on one EC2 instance at a time, while EFS can be mounted on multiple EC2 instances at the same time. EBS is only available in one AZ, while EFS is available in all AZs in the region and EFS automatically scales up to petabytes.

## Classes

- Standard
- Infrequent Access (EFS-IA)

## Billing

- Pay for the storage you use not for capacity (no pre-provisioning required).
