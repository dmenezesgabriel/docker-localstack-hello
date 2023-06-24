# Elastic Load Balancer (ELB)

## Description

Load Balancer is a service that distributes incoming traffic across multiple targets, such as Amazon EC2 instances, containers, IP addresses, and Lambda functions. You can load balance all types of traffic, including HTTP, HTTPS, TCP, and WebSockets.

## Types

### Application Load Balancer

Application Load Balancer is best suited for load balancing of HTTP and HTTPS traffic and provides advanced request routing targeted at the delivery of modern application architectures, including microservices and containers.

#### OSI - Layer 7

Application Load Balancer operates at the application layer (layer 7) and supports HTTP and HTTPS applications and WebSockets.

### Network Load Balancer

Network Load Balancer is best suited for load balancing of Transmission Control Protocol (TCP), User Datagram Protocol (UDP), and Transport Layer Security (TLS) traffic where extreme performance is required.

#### OSI - Layer 4

Network Load Balancer operates at the transport layer (layer 4) and supports TCP, UDP, and TLS (Layer 7) protocols.

## OSI

OSI: Open Systems Interconnection

OSI is a conceptual framework used to describe the functions of a networking system.
