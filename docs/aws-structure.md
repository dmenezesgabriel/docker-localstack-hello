# AWS Structure

[global infrastructure](https://aws.amazon.com/pt/about-aws/global-infrastructure/)

## Region

Regions are geographical areas divided by AWS to host their services. Each region is a separate geographic area. Each region has multiple, isolated locations known as Availability Zones. Each region is completely independent. Each Availability Zone is isolated, but the Availability Zones in a region are connected through low-latency links. Each Availability Zone is designed as an independent failure zone. This means that Availability Zones are physically separated within a typical metropolitan region and are located in lower-risk flood plains (specific flood zone categorization varies by Region). In addition to discrete uninterruptible power supply (UPS) and onsite backup generation facilities, they are each fed via different grids from independent utilities to further reduce single points of failure. Availability Zones are all redundantly connected to multiple tier-1 transit providers.

- America/Sao_Paulo
- America/New_York
- Europe/London
- Asia/Tokyo
- ...

### Choosing a Region

- Compliance with data governance and legal requirements: some countries have laws that require data to be stored in a specific region
- Proximity to customers: lower latency
- Available services: not all services are available in all regions
- Pricing: some regions are more expensive than others

## Availability Zones (AZ)

Is a logical data center in a region, each AZ is supported by one or more physical data centers nearby, with redundant power, networking and connectivity, housed in separate facilities. Partitioned applications can be deployed across multiple AZs to achieve high availability and also to be protected against natural disasters like floods, tornados, earthquakes, etc.

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

### Services

- [Route 53](aws-route53.md)
- [CloudFront](aws-cloudfront.md)
- [AWS Outposts](aws-outposts.md)
