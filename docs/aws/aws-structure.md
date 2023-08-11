# AWS Structure

[global infrastructure](https://aws.amazon.com/pt/about-aws/global-infrastructure/)

Why make a global application?

- Decrease latency
- Disaster recovery
- Attack protection

## Region

Regions are geographical areas divided by AWS to host their services. Each region is a separate geographic area. Each region has multiple, isolated locations known as Availability Zones. Each region is completely independent. Each Availability Zone is isolated, but the Availability Zones in a region are connected through low-latency links. Each Availability Zone is designed as an independent failure zone.

A Region is a named set of AWS resources in the same geographic area. A Region comprises at least two Availability Zones. Regions would be the appropriate way to replicate data in a Disaster Recovery plan.

In short, a region is a physical location in the world that consists of two or more Availability Zones (AZs). AWS has 24 regions around the world, and 77 Availability Zones.

- America/Sao_Paulo
- America/New_York
- Europe/London
- Asia/Tokyo
- ...

Offers global storage and compute power implementation.

### Choosing a Region

- Compliance with data governance and legal requirements: some countries have laws that require data to be stored in a specific region
- Proximity to customers: lower latency
- Available services: not all services are available in all regions
- Pricing: some regions are more expensive than others

## Availability Zones (AZ)

Is a logical data center in a region, each AZ is supported by one or more physical data centers nearby, with redundant power, networking and connectivity, housed in separate facilities. Partitioned applications can be deployed across multiple AZs to achieve high availability.

- north
- east
- south
- west

Example:

- us-east-1a
- us-east-1b
- us-east-1c
- us-east-1d

### Advices

- Always use more than one AZ in a region.

## Edge Locations

An edge location is a site that Amazon CloudFront uses to cache copies of your content for faster delivery to users at any location. There are more edge locations than regions.

### Services

- [CloudFront](aws-cloudfront.md)
- [Route 53](aws-route53.md)
- [Lambda@Edge](aws-lambda.md#lambdaedge)
- [API Gateway](aws-api-gateway.md)
- [WAF & Shield](aws-waf.md)
- [S3 Transfer Acceleration](aws-s3.md#transfer-acceleration)
- [Direct Connect](aws-direct-connect.md)
- ...

### Use cases

- Distribute content to end users with low latency
- Deliver streaming videos
- Distribute software and game updates
- Provide a secure, fast, and reliable way to put your data in AWS
