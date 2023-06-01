# Storage Gateway

## Description

- Hardware appliance that provides your applications with access to virtually unlimited storage in AWS Cloud.
- Hybrid cloud storage service that gives you on-premises access to virtually unlimited cloud storage.
- Connect on-premises software appliance with cloud-based storage to provide seamless and secure integration between an organization's on-premises IT environment and AWS's storage infrastructure.

## Usage Types

- File Gateway (NFS): Store and retrieve objects as files using NFSv3 or NFSv4.1 protocol.
- Volume Gateway (iSCSI): Store data in volumes using the iSCSI block protocol.
  - Stored Volumes: Entire dataset is stored on-site and asynchronously backed up to S3.
  - Cached Volumes: Entire dataset is stored on S3 and the most frequently accessed data is cached on-site.
- Tape Gateway (VTL): Backup data in the cloud using industry-standard storage protocols, that is, iSCSI and VTL.
