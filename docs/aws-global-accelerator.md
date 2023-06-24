# AWS Global accelerator

## Description

AWS Global Accelerator is a service that improves the availability and performance of your applications with local or global users. It provides static IP addresses that act as a fixed entry point to your application endpoints in a single or multiple AWS Regions, such as your Application Load Balancers, Network Load Balancers or Amazon EC2 instances.

It can be used to launch an application in a single AWS Region to a worldwide user base.

## Anycast IP

AWS Global Accelerator uses Anycast IP addresses to direct traffic to the optimal endpoint. Anycast is a networking and routing technology that helps route traffic to the nearest AWS Region. It does this by announcing the same IP address from multiple AWS edge locations around the world.

## Global Accelerator vs CloudFront vs Edge Locations

AWS Global Accelerator is not a content delivery network (CDN) like Amazon CloudFront. It does not cache content or route traffic to multiple locations for increased global availability. Instead, it uses the AWS global network to optimize the path from your users to your applications, improving the performance of TCP and UDP traffic.
