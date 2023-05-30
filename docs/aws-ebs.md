# EBS

Elastic Block Store (EBS) is a block storage service that you can use to store data persistently. EBS volumes are placed in a specific Availability Zone, where they are automatically replicated to protect you from the failure of a single component.

It must be always in the same availability zone of your EC2 instance. To access in another availability zone, you must create a snapshot and copy to another availability zone.

## Use cases

- Boot volume for EC2 instances.
- Database storage.
- File system storage.
- Application storage.

## Types

- General Purpose SSD (gp2): General purpose, balance between price and performance.
- General Purpose SSD (gp3): General purpose, balance between price and performance.
- Provisioned IOPS SSD (io1): High performance, for critical applications.
- Throughput Optimized HDD (st1): Low cost, frequently accessed, throughput intensive workloads.
- Cold HDD (sc1): Lowest cost, less frequently accessed, throughput intensive workloads.
- Magnetic (standard): Lowest cost per gigabyte, for workloads where data is accessed infrequently, and applications where the lowest storage cost is important.
