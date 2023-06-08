# EC2

Elastic Compute Cloud

## Benefits

- Eliminates upfront hardware investment

## Plans

- On Demand
- Reserved Instances
- Dedicated Hosts
- Spot instances

## siglas

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

#### Types

##### SSD

- General Purpose SSD (GP2): General purpose, balances price and performance.
- General Purpose SSD (GP3): General purpose, balances price and performance.
- Provisioned IOPS SSD (IO1): Designed for I/O intensive applications such as large relational or NoSQL databases.

GP3 vs GP2: GP3 is 20% cheaper than GP2, but it has a minimum of 3000 IOPS and a maximum of 16000 IOPS. GP2 has a minimum of 100 IOPS and a maximum of 16000 IOPS.

##### HDD

- Throughput Optimized HDD (ST1): Low cost HDD volume designed for frequently accessed, throughput intensive workloads.
- Cold HDD (SC1): Lowest cost HDD volume designed for less frequently accessed workloads.

## AMI - Amazon Machine Image

Provides the information required to launch an instance, which is a virtual server in the cloud. You must specify a source AMI when you launch an instance. You can launch multiple instances from a single AMI when you need multiple instances with the same configuration. You can use different AMIs to launch instances when you need instances with different configurations.
