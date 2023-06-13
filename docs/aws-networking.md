# Networking

> Who should be able to communicate with each other?

## VPC

Virtual Private Cloud (VPC) is a virtual network dedicated to your AWS account. It is logically isolated from other virtual networks in the AWS Cloud. You can launch your AWS resources, such as Amazon EC2 instances, into your VPC.

Imagine a million of customers who use AWS Services, also the millions of resources that they use. How does AWS keep all of these resources separate? The answer is VPC. VPC is a virtual network that is logically isolated from other virtual networks in the AWS Cloud. You can launch your AWS resources, such as Amazon EC2 instances, into your VPC.

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

## Virtual Private Gateway

A virtual private gateway is the VPN concentrator on the Amazon side of the VPN connection between your on-premises network and your VPC.

## Direct Connect Gateway

A Direct Connect gateway is a globally available resource. It is a virtual private gateway that is automatically attached to your Direct Connect connection at the time of creation. You can associate up to three transit gateways with a Direct Connect gateway.

## Network Access Control List (NACL)

A network access control list (ACL) is an optional layer of security for your VPC that acts as a firewall for controlling traffic in and out of one or more subnets.

- stateless

## Security Group

A security group acts as a virtual firewall for your instance to control inbound and outbound traffic. When you launch an instance in a VPC, you can assign up to five security groups to the instance. Security groups act at the instance level, not the subnet level. Therefore, each instance in a subnet in your VPC could be assigned to a different set of security groups. If you don't specify a particular group at launch time, the instance is automatically assigned to the default security group for the VPC.

- stateful
