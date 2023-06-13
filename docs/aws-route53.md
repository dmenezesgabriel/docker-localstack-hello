# Route 53

DNS: Domain Name System

- DNS is a globally distributed service that translates human readable names like www.example.com into the numeric IP addresses.

## Routing Policies

### Latency-based Routing

- Use when you have resources in multiple AWS Regions and you want to route traffic to the region that provides the best latency.

### Geolocation Routing

- Use when you want to route traffic based on the location of your users.

### Geoproximity Routing

- Use when you want to route traffic based on the location of your resources and, optionally, shift traffic from resources in one location to resources in another.

### Weighted Routing robin

- Use to route traffic to multiple resources in proportions that you specify.
