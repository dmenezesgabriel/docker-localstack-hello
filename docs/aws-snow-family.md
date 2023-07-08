# Snow Family

- [Snow Family](https://aws.amazon.com/snow/)

The Snow Family is a collection of physical devices for moving data into and out of AWS. The devices are ruggedized, secure, and proven to move data in and out of

- [Snowcone](aws-snow-family.md#snowcone)
- [Snowball](aws-snow-family.md#snowball)
- [Snowmobile](aws-snow-family.md#snowmobile)

## Data Migration

Why to make data migration with snow family? Because it is faster and cheaper than over the internet. If it takes more than a week to transfer data over the internet, it is cheaper to use Snowball.

- Snowcone
- Snowball Edge
- Snowmobile

| Snowmobile     | Snowball        | Snowcone        |
| -------------- | --------------- | --------------- |
| 100 PB         | 80 TB           | 8 TB            |
| UP to exabytes | Up to petabytes | Up to terabytes |

## Edge Computing

Process data while it's being created on the edge, and then transfer it to AWS. Ex: a truck on the road, a ship on the sea, a mining station underground...

- Snowcone
- Snowball Edge

These locations may have:

- Limited / no internet access
- Limited / no easy access to computing power

Use cases:

- Preprocess data before sending to AWS
- Machine learning at the edge
- Transcoding media files

## Snowcone

- [Snowcone](https://aws.amazon.com/snowcone/)

Snowcone is the smallest member of the Snow Family of devices, designed for edge computing and data transfer in harsh environments. Snowcone is portable, rugged, and secure – small and light enough to fit in a backpack, and able to withstand harsh environments.

Used when Snowball does not fit (space-constrained environments).

## Snowball edge

- [Snowball](https://aws.amazon.com/snowball-edge/)

Snowball is a petabyte-scale data transport solution that uses secure appliances to transfer large amounts of data into and out of AWS. Using Snowball addresses common challenges with large-scale data transfers including high network costs, long transfer times, and security concerns.

### Edge Storage Optimized

- [Snowball Edge Storage Optimized](https://aws.amazon.com/snowball-edge/)

Snowball Edge Storage Optimized devices provide both block storage and Amazon S3-compatible object storage, 80 TB of HDD capacity, and 40 vCPUs. Snowball Edge Storage Optimized devices are well suited for local storage and large-scale data transfer, or as a temporary storage tier for large local datasets. Snowball Edge Storage Optimized devices are well suited for local storage and large-scale data transfer, or as a temporary storage tier for large local datasets.

### Compute Optimized

- [Snowball Edge Compute Optimized](https://aws.amazon.com/snowball-edge/)

Snowball Edge Compute Optimized devices provide 52 vCPUs, 208 GiB of RAM, and an optional GPU for use in edge computing workloads. Snowball Edge Compute Optimized devices are well suited for local processing and machine learning workloads.

Use cases: large data cloud migrations, disaster recovery, data center decommission, content distribution, video capture, machine learning and analytics, IoT, and genomics.

## Snowmobile

- [Snowmobile](https://aws.amazon.com/snowmobile/)

Snowmobile is an Exabyte-scale data transfer service used to move extremely large amounts of data to AWS. You can transfer up to 100PB per Snowmobile, a 45-foot long ruggedized shipping container, pulled by a semi-trailer truck. Snowmobile makes it easy to move massive volumes of data to the cloud, including video libraries, image repositories, or even a complete data center migration.
100 PB Data

## AWS OpsHub

- [AWS OpsHub](https://aws.amazon.com/snowball/resources/ops-hub/)

AWS OpsHub is a web-based application that helps you manage your Snow Family devices. You can use OpsHub to create jobs, manage devices, and monitor the status of your jobs and devices.
