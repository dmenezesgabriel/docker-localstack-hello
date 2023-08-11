# AWS Route 53

## Description

### Domain Name System (DNS)

DNS is a globally distributed service that translates human readable names like www.example.com into the numeric IP addresses.

## Routing Policies

### Simple Routing

- Use when you have a single resource that performs a given function for your domain, for example, one web server that serves content for the example.com website.

### Weighted Routing

- Use to route traffic to multiple resources in proportions that you specify.

### Latency-based Routing

- Use when you have resources in multiple AWS Regions and you want to route traffic to the region that provides the best latency.

### Failover Routing

- Use when you want to configure active-passive failover.
