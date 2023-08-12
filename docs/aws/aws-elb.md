# Elastic Load Balancer (ELB)

## Description

Load Balancer is a service that distributes incoming traffic across multiple targets, such as Amazon **EC2, ECS and EKS** instances, containers, IP addresses, and Lambda functions. You can load balance all types of traffic, including HTTP, HTTPS, TCP, and WebSockets.

- Fault tolerance
- High availability

## Types

### Application Load Balancer (Layer 7)

Application Load Balancer is best suited for load balancing of HTTP and HTTPS traffic and provides advanced request routing targeted at the delivery of modern application architectures, including microservices and containers.

### Network Load Balancer (Layer 4)

Network Load Balancer is best suited for load balancing of Transmission Control Protocol (TCP), User Datagram Protocol (UDP), and Transport Layer Security (TLS) traffic where extreme performance is required.

### Gateway Load Balancer (Layer 3)

Gateway Load Balancer is a new type of load balancer that allows you to deploy, scale, and manage third-party virtual appliances such as firewalls, intrusion detection and prevention systems, analytics, and other virtual appliances.

### CLassic Load Balancer (layer 4 and 7)

Classic Load Balancer provides basic load balancing across multiple Amazon EC2 instances and operates at both the request level and connection level. Classic Load Balancer is intended for applications that were built within the EC2-Classic network.

## Target Groups

A target group tells a load balancer where to direct traffic to. You can add multiple targets to a target group. When you create each listener rule, you specify a target group and conditions. When a rule condition is met, traffic is forwarded to the corresponding target group. You can create different target groups for different types of requests. For example, create one target group for general requests and other target groups for requests to the microservices for your application.

- [Auto Scaling](aws-scaling.md#auto-scaling-group)
