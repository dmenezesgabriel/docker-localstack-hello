# EC2

Elastic Compute Cloud

## Benefits

- Eliminates upfront hardware investment
- It can run customer managed databases

## Plans

- On Demand
- Reserved Instances
- Dedicated Hosts
- Spot instances

## Instance Types

[EC2 Instance Types](https://aws.amazon.com/pt/ec2/instance-types/)
[Instances detail](https://instances.vantage.sh/)

### General Purpose

General purpose instances provide a balance of compute, memory, and networking resources, and can be used for a variety of diverse workloads, such as:

- Small and mid-size databases
- application servers
- gaming servers
- backend servers for enterprise applications

Prefixes: A, T, M

### Compute Optimized

Compute optimized instances are ideal for compute-bound applications that benefit from high-performance processors. Compute optimized instances are well suited for compute-intensive applications such as:

- High performance web servers
- High performance computing (HPC)
- Scientific modelin/1g
- Dedicated gaming servers
- Machine learning inference
- Batch processing workloads

Prefixes: C

### Memory Optimized

Memory optimized instances are designed to deliver fast performance for workloads that process large data sets in memory. Memory optimized instances are ideal for high-performance databases, distributed web scale in-memory caches, mid-size in-memory databases, real time big data analytics, and other enterprise applications.

Prefixes: R, X

### Accelerated Computing

Accelerated computing instances use hardware accelerators, or co-processors, to perform some functions, such as floating point number calculations, graphics processing, or data pattern matching, more efficiently than is possible in software running on CPUs. Accelerated computing instances are ideal for workloads such as:

- Graphics applications
- Game streaming
- Application streaming
- Video encoding
- Data visualization
- High performance computing (HPC)
- Machine learning inference

Prefixes: P, G, F

#### CPU vs GPU

- **CPU**: CPUs are ideal for tasks that require high single-threaded performance, such as general-purpose computing, web browsing, office applications, and running most software applications.
- **GPU**: GPUs are ideal for tasks that involve parallel processing, such as gaming, video editing, 3D rendering, machine learning, cryptocurrency mining, and scientific simulations. They excel in applications that can split large amounts of data into smaller tasks that can be processed simultaneously.

### Storage Optimized

Storage optimized instances are designed for workloads that require high, sequential read and write access to very large data sets on local storage. They are optimized to deliver tens of thousands of low-latency, random I/O operations per second (IOPS) to applications. Storage optimized instances are ideal for high frequency online transaction processing (OLTP) systems, relational and NoSQL databases, cache for in-memory databases, data warehousing applications, distributed file systems, and big data workload

Prefixes: I, D

#### IOPS

IOPS (Input/Output Operations Per Second, pronounced eye-ops) is a common performance measurement used to benchmark computer storage devices like hard disk drives (HDD), solid state drives (SSD), and storage area networks (SAN). As the name implies, IOPS measures the maximum number of reads and writes to non-contiguous storage locations. For example, a hard drive with 200 IOPS can perform 200 data transfers per second.

## Storages (Volumes)

Measure: IOPS (Input/ Output per second)

- [EBS](aws-ebs.md): Elastic block storage
- [EFS](aws-efs.md): Elastic file system

## AMI - Amazon Machine Image

Provides the information required to launch an instance, which is a virtual server in the cloud. You must specify a source AMI when you launch an instance. You can launch multiple instances from a single AMI when you need multiple instances with the same configuration. You can use different AMIs to launch instances when you need instances with different configurations.

The AMI must be in the same region as that of the EC2 instance to be launched. If the AMI exists in a different region, you can copy that AMI to the region where you want to launch the EC2 instance. The region of AMI has no bearing on the performance of the EC2 instance.

## EC2 Image Builder

Automatically build, test and distribute AMIs.

## EC2 Instance Store

High performance hardware disk attached to our EC2 instance, but is lost if instance is stopped or terminated

**It offers a temporary block-level storage.**

## Pricing

With Amazon EC2, you pay for only the compute time you use while your instances are running. You are billed only for the instances you launch, and only fr as long as they are running.

For some workloads (e.g. web servers), you can use Amazon EC2 Spot Instances to take advantage of unused EC2 capacity in the AWS cloud. Spot Instances are available at up to a 90% discount compared to On-Demand prices.

### On Demand

On-Demand instances are ideal for short-term, irregular workloads that cannot be interrupted. No upfront payment or long-term commitment is required. You pay only for the hours that you use.

This model works like a pay-as-you-go mobile phone plan: you pay for what you use and you pay for as long as you need it.

### AWS EC2 Savings Plans

Savings Plans is a flexible pricing model that provides savings of up to 72% on your AWS compute usage. This pricing model offers lower prices on Amazon EC2 instances usage, regardless of instance family, size, OS, tenancy or AWS Region, and also applies to AWS Fargate usage.

This model works like a contract, where you commit to a consistent amount of compute usage (measured in $/hour) for a 1 or 3 year term, and in exchange you receive a discount on that usage. You can choose between two different types of Savings Plans: Compute Savings Plans and EC2 Instance Savings Plans.

### Reserved Instances

Reserved Instances provide you with a significant discount (up to 75%) compared to On-Demand instance pricing. In addition, when Reserved Instances are assigned to a specific Availability Zone, they provide a capacity reservation, giving you additional confidence in your ability to launch instances when you need them.

This model works like a contract, where you commit to a consistent amount of compute usage (measured in $/hour) for a 1 or 3 year term, and in exchange you receive a discount on that usage. You can choose between two different types of Reserved Instances: Standard Reserved Instances and Convertible Reserved Instances.

#### Reserved Instances vs Savings Plans

In summary the main differences between Reserved Instances and Savings Plans are:

- **Instance Size Flexibility**: Savings Plans provide you with the flexibility to change instance families, sizes, OS types, and tenancies within a specific AWS Region. Reserved Instances are purchased for a specific instance family, size, and Region, and provide a capacity reservation when used in a specific Availability Zone.

- **Term Commitment**: Savings Plans provide you with the flexibility to change your compute usage over time. Reserved Instances provide you with a capacity reservation when used in a specific Availability Zone, and provide a significant discount compared to On-Demand Instance pricing.

- **Payment Options**: Savings Plans provide you with the flexibility to pay for your compute usage in one of two ways: All Upfront or On Demand. Reserved Instances provide you with the flexibility to pay for your compute usage in one of three ways: All Upfront, Partial Upfront, or No Upfront.

### Spot Instances

Spot Instances allow you to request spare Amazon EC2 computing capacity for up to 90% off the On-Demand price. Spot Instances are available at a discount compared to On-Demand pricing, and you pay the Spot price that's in effect for the time period your instances are running. Spot Instances are a cost-effective choice if you can be flexible about when your applications run and if your applications can be interrupted.

This model works like an auction, where you bid for the price you are willing to pay for a compute capacity. If the current Spot price is lower than your bid, your instances will run. If the Spot price goes above your bid, your instances will be terminated.

### Dedicated Hosts

Dedicated Hosts are physical servers with EC2 instance capacity fully dedicated to your use. Dedicated Hosts can help you address compliance requirements and reduce costs by allowing you to use your existing server-bound software licenses.

This model works like a contract, where you commit to a consistent amount of compute usage (measured in $/hour) for a **1 or 3** year term, and in exchange you receive a discount on that usage.

**Important!**: Instance stores can be lost if the instance is stopped or terminated, use [EBS](aws-ebs.md) instead.

## Related

- [Load Balancer](aws-elb.md)
- [Auto Scaling](aws-scaling.md)
- [Elastic Block Storage](aws-ebs.md)
- [Elastic File System](aws-efs.md)

## Aditional info

- There is a one-minute minimum charge for Linux based EC2 instances:w
