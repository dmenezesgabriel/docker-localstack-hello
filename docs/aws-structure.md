# AWS Structure

[global infrastructure](https://aws.amazon.com/pt/about-aws/global-infrastructure/)

## Region

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

### Edge Locations

- Smaller Data Centers

Purpose:

static information

- caching
- cdn
- cloud front
