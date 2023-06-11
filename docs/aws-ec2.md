# EC2

Elastic Compute Cloud

## Benefits

- Eliminates upfront hardware investment

## Plans

- On Demand
- Reserved Instances
- Dedicated Hosts
- Spot instances

## EC2 Types

- c: Compute opt
- g: Graphics
- d: Dense storage
- r: Memory opt
- m: General
- i: High speed storage
- f: Programming
- t: web servers
- p: gpu (ex: mining)
- x: memory (ex: apache)

### General Purpose

General purpose instances provide a balance of compute, memory, and networking resources, and can be used for a variety of diverse workloads, such as:

- Small and mid-size databases
- application servers
- gaming servers
- backend servers for enterprise applications

### Compute Optimized

Compute optimized instances are ideal for compute-bound applications that benefit from high-performance processors. Compute optimized instances are well suited for compute-intensive applications such as:

- High performance web servers
- High performance computing (HPC)
- Scientific modeling
- Dedicated gaming servers
- Machine learning inference

### Memory Optimized

Memory optimized instances are designed to deliver fast performance for workloads that process large data sets in memory. Memory optimized instances are ideal for high-performance databases, distributed web scale in-memory caches, mid-size in-memory databases, real time big data analytics, and other enterprise applications.

### Accelerated Computing

Accelerated computing instances use hardware accelerators, or co-processors, to perform some functions, such as floating point number calculations, graphics processing, or data pattern matching, more efficiently than is possible in software running on CPUs. Accelerated computing instances are ideal for workloads such as:

- Graphics applications
- Game streaming
- Application streaming
- Video encoding
- Data visualization
- High performance computing (HPC)
- Machine learning inference

#### CPU vs GPU

- **CPU**: CPUs are ideal for tasks that require high single-threaded performance, such as general-purpose computing, web browsing, office applications, and running most software applications.
- **GPU**: GPUs are ideal for tasks that involve parallel processing, such as gaming, video editing, 3D rendering, machine learning, cryptocurrency mining, and scientific simulations. They excel in applications that can split large amounts of data into smaller tasks that can be processed simultaneously.

### Storage Optimized

Storage optimized instances are designed for workloads that require high, sequential read and write access to very large data sets on local storage. They are optimized to deliver tens of thousands of low-latency, random I/O operations per second (IOPS) to applications. Storage optimized instances are ideal for high frequency online transaction processing (OLTP) systems, relational and NoSQL databases, cache for in-memory databases, data warehousing applications, distributed file systems, and big data workload

#### IOPS

IOPS (Input/Output Operations Per Second, pronounced eye-ops) is a common performance measurement used to benchmark computer storage devices like hard disk drives (HDD), solid state drives (SSD), and storage area networks (SAN). As the name implies, IOPS measures the maximum number of reads and writes to non-contiguous storage locations. For example, a hard drive with 200 IOPS can perform 200 data transfers per second.

## Storages (Volumes)

Measure: IOPS (Input/ Output per second)

- EBS: Elastic block storage
- EF2: Elastic file system
- GP2: SSD
- Provisioned: High Intensity (ex: MySQL, SQL)
- ST1: HDD, cannot be used to boot an Operational System
- SC1: Cold HDD, for infrequent access, it cannot be used to boot an operational system.
- Magnet (Standard): It accepts to boot operational system

### EBS

Elastic Block Storage is a storage device that can be attached to an EC2 instance. It is a network drive that you can attach to your instances while they run. It allows your instances to persist data, even after their termination.

- Each EBS volume can be attached to only one EC2 instance at a time.
- Multiple volumes of EBS can be attached to the same EC2 instance.
- Snapshot: It is a backup of your EBS volume at a point in time. It is stored in S3.
- Single digit millisecond latency.
- Dinamically change the configuration of the volume (size, type, IOPS) without stopping the instance.
- CloudWatch and Lambda can be used to automate the process of creating snapshots and also volume changes.
- 99.999% availability.
- Automatically replicated within its Availability Zone to protect you from component failure, offering high availability and durability.

#### EBS Types

##### SSD

- General Purpose SSD (GP2): General purpose, balances price and performance.
- General Purpose SSD (GP3): General purpose, balances price and performance.
- Provisioned IOPS SSD (IO1): Designed for I/O intensive applications such as large relational or NoSQL databases.
- Provisioned IOPS SSD (IO2): Designed for I/O intensive applications such as large relational or NoSQL databases.

GP3 vs GP2: GP3 is 20% cheaper than GP2, but it has a minimum of 3000 IOPS and a maximum of 16000 IOPS. GP2 has a minimum of 100 IOPS and a maximum of 16000 IOPS.
IO2 vs IO1: IO2 is 15% cheaper than IO1, but it has a minimum of 100 IOPS and a maximum of 64000 IOPS. IO1 has a minimum of 100 IOPS and a maximum of 64000 IOPS.

##### HDD

- Throughput Optimized HDD (ST1): Low cost HDD volume designed for frequently accessed, throughput intensive workloads.
- Cold HDD (SC1): Lowest cost HDD volume designed for less frequently accessed workloads.

##### Amazon EBS Volume Comparison

| Subject                   | io2     | io2 Block Express | io3     | gp3        | gp2        | st1      | sc1      |
| ------------------------- | ------- | ----------------- | ------- | ---------- | ---------- | -------- | -------- |
| Latency (single digit ms) | Yes     | Yes               | Yes     | Yes        | Yes        | Yes      | Yes      |
| Baseline Burst            | -       | -                 | -       | 3000 IOPS  | 3000 IOPS  | 500 IOPS | 250 IOPS |
| Maximum IOPS Volume       | 64000   | 64000             | 64000   | 16000 IOPS | 16000 IOPS | 500 IOPS | 250 IOPS |
| Maximum Throughput Volume | 1000    | 4000              | 1000    | 1000 MB/s  | 250 MB/s   | 500 MB/s | 250 MB/s |
| Volume Size               | 4 TiB   | 64 TiB            | 16 TiB  | 16 TiB     | 16 TiB     | 16 TiB   | 16 TiB   |
| Availability              | 99.999% | 99.999%           | 99.999% | 99.99%     | 99.99%     | 99.99%   | 99.99%   |

#### Snapshots

Snapshots exist on S3 and are incremental, which means that only the blocks that have changed since your last snapshot are moved to S3.

##### Amazon Data Lifecycle Manager

Automates the creation, retention, and deletion of snapshots taken to back up your EBS volumes.

## AMI - Amazon Machine Image

Provides the information required to launch an instance, which is a virtual server in the cloud. You must specify a source AMI when you launch an instance. You can launch multiple instances from a single AMI when you need multiple instances with the same configuration. You can use different AMIs to launch instances when you need instances with different configurations.

## Pricing

### On Demand

On-Demand instances are ideal for short-term, irregular workloads that cannot be interrupted. No upfront payment or long-term commitment is required. You pay only for the hours that you use.

This model works like a pay-as-you-go mobile phone plan: you pay for what you use and you pay for as long as you need it.

### AWS EC2 Savings Plans

Savings Plans is a flexible pricing model that provides savings of up to 72% on your AWS compute usage. This pricing model offers lower prices on Amazon EC2 instances usage, regardless of instance family, size, OS, tenancy or AWS Region, and also applies to AWS Fargate usage.

This model works like a contract, where you commit to a consistent amount of compute usage (measured in $/hour) for a 1 or 3 year term, and in exchange you receive a discount on that usage. You can choose between two different types of Savings Plans: Compute Savings Plans and EC2 Instance Savings Plans.

### Reserved Instances

Reserved Instances provide you with a significant discount (up to 75%) compared to On-Demand instance pricing. In addition, when Reserved Instances are assigned to a specific Availability Zone, they provide a capacity reservation, giving you additional confidence in your ability to launch instances when you need them.

This model works like a contract, where you commit to a consistent amount of compute usage (measured in $/hour) for a 1 or 3 year term, and in exchange you receive a discount on that usage. You can choose between two different types of Reserved Instances: Standard Reserved Instances and Convertible Reserved Instances.

### Spot Instances

Spot Instances allow you to request spare Amazon EC2 computing capacity for up to 90% off the On-Demand price. Spot Instances are available at a discount compared to On-Demand pricing, and you pay the Spot price that's in effect for the time period your instances are running. Spot Instances are a cost-effective choice if you can be flexible about when your applications run and if your applications can be interrupted.

This model works like an auction, where you bid for the price you are willing to pay for a compute capacity. If the current Spot price is lower than your bid, your instances will run. If the Spot price goes above your bid, your instances will be terminated.

### Dedicated Hosts

Dedicated Hosts are physical servers with EC2 instance capacity fully dedicated to your use. Dedicated Hosts can help you address compliance requirements and reduce costs by allowing you to use your existing server-bound software licenses.

This model works like a contract, where you commit to a consistent amount of compute usage (measured in $/hour) for a 1 or 3 year term, and in exchange you receive a discount on that usage.
