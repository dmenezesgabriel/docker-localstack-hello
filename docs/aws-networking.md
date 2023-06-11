# Networking

## VPC

Virtual Private Cloud (VPC) is a virtual network dedicated to your AWS account. It is logically isolated from other virtual networks in the AWS Cloud. You can launch your AWS resources, such as Amazon EC2 instances, into your VPC.

Imagine a million of customers who use AWS Services, also the millions of resources that they use. How does AWS keep all of these resources separate? The answer is VPC. VPC is a virtual network that is logically isolated from other virtual networks in the AWS Cloud. You can launch your AWS resources, such as Amazon EC2 instances, into your VPC.

## Subnet

A subnet is a range of IP addresses in your VPC. You can launch AWS resources into a specified subnet. Use a public subnet for resources that must be connected to the internet, and a private subnet for resources that won't be connected to the internet.

## Internet Gateway

An internet gateway is a horizontally scaled, redundant, and highly available VPC component that allows communication between your VPC and the internet. It therefore imposes no availability risks or bandwidth constraints on your network traffic.

## Virtual Private Gateway

A virtual private gateway is the VPN concentrator on the Amazon side of the VPN connection between your on-premises network and your VPC.

## Direct Connect Gateway

A Direct Connect gateway is a globally available resource. It is a virtual private gateway that is automatically attached to your Direct Connect connection at the time of creation. You can associate up to three transit gateways with a Direct Connect gateway.
