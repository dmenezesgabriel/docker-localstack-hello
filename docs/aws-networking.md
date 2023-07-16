# AWS Networking

> Who should be able to communicate with each other?

## Description

In short, AWS Networking is the process of connecting resources in a virtual network.

## VPC

Virtual Private Cloud (VPC) is a virtual network dedicated to your AWS account. It is logically isolated from other virtual networks in the AWS Cloud. You can launch your AWS resources, such as Amazon EC2 instances, into your VPC.

Imagine a million of customers who use AWS Services, also the millions of resources that they use. How does AWS keep all of these resources separate? The answer is VPC. VPC is a virtual network that is logically isolated from other virtual networks in the AWS Cloud. You can launch your AWS resources, such as Amazon EC2 instances, into your VPC.

- Flow logs: capture information about IP traffic going to and from network interfaces in your VPC.

### VPC Peering

VPC peering connection is a networking connection between two VPCs that enables you to route traffic between them using private IPv4 addresses or IPv6 addresses. Instances in either VPC can communicate with each other as if they are within the same network.

### VPC Endpoints

A VPC endpoint enables you to privately connect your VPC to supported AWS services and VPC endpoint services powered by AWS PrivateLink without requiring an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection. Instances in your VPC do not require public IP addresses to communicate with resources in the service. Traffic between your VPC and the other service does not leave the Amazon network.

#### AWS PrivateLink

AWS PrivateLink is a technology that enables you to privately access services by using private IP addresses. AWS PrivateLink restricts all network traffic between your VPC and other services to the Amazon network. AWS PrivateLink provides private connectivity between VPCs, AWS services, and on-premises applications, securely on the Amazon network.

## Subnet

A subnet is a range of IP addresses in your VPC. You can launch AWS resources into a specified subnet. Use a public subnet for resources that must be connected to the internet, and a private subnet for resources that won't be connected to the internet.

### Public Subnet

A public subnet is a subnet that is associated with a route table that has a route to an internet gateway.

It contains resources that can be accessed by the public, such as an online store's website.

### Private Subnet

A private subnet is a subnet that is associated with a route table that does not have a route to an internet gateway.

It contains resources that cannot be accessed by the public, such as a database.

## Internet Gateway

An internet gateway is a horizontally scaled, redundant, and highly available VPC component that allows communication between your VPC and the internet. It therefore imposes no availability risks or bandwidth constraints on your network traffic.

## NAT Gateway

A NAT gateway is a device that enables instances in a private subnet to connect to the internet or other AWS services, but prevents the internet from initiating a connection with those instances.

## Virtual Private Gateway

A virtual private gateway is the VPN concentrator on the Amazon side of the VPN connection between your on-premises network and your VPC.

## Direct Connect Gateway

A Direct Connect gateway is a globally available resource. It is a virtual private gateway that is automatically attached to your Direct Connect connection at the time of creation. You can associate up to three transit gateways with a Direct Connect gateway.

## Network Access Control List (NACL)

A network access control list (ACL) is an optional layer of security for your VPC that acts as a firewall for controlling traffic in and out of one or more subnets.

- stateless
- at subnet level

## Security Group

A security group acts as a virtual firewall for your instance to control inbound and outbound traffic. When you launch an instance in a VPC, you can assign up to five security groups to the instance. Security groups act at the instance level, not the subnet level. Therefore, each instance in a subnet in your VPC could be assigned to a different set of security groups. If you don't specify a particular group at launch time, the instance is automatically assigned to the default security group for the VPC.

- stateful
- at instance level

**inbound**: traffic coming into the instance.
**outbound**: traffic going out of the instance.

## Site to Site VPN

A site-to-site VPN connection connects your on-premises network to your Amazon VPC over an IPsec VPN tunnel. This enables you to securely access your AWS resources as if they were hosted on your on-premises network.

- CGW: Customer Gateway
- VGW: Virtual Private Gateway

## AWS Client VPN

AWS Client VPN is a managed client-based VPN service that enables you to securely access your AWS resources or your on-premises network. With AWS Client VPN, you can access your resources from any location using an OpenVPN-based VPN client.

## Transit Gateway

A transit gateway is a network transit hub that you can use to interconnect your virtual private clouds (VPC) and on-premises networks. Transit gateways enable you to create a hub-and-spoke network topology, where you can interconnect your VPCs and data centers using a single gateway.
