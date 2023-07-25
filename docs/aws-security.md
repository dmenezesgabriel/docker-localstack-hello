# Security

## Shield standard

Shield standard is a free service that protects your website from DDoS attacks.

## Shield advanced

Shield advanced is a paid service that protects your website from DDoS attacks. It includes a web application firewall (WAF) that can be used to block malicious traffic.

**DDoS** stands for Distributed Denial of Service. It is a type of attack that is used to make a website unavailable by flooding it with traffic.

## KMS

KMS (Key Management Service) is a service that allows you to create and manage encryption keys. It is used by other AWS services to encrypt data at rest.

## GuardDuty

Amazon GuardDuty is a service that provides intelligent threat detection for your AWS infrastructure and resources. It identifies threats by continuously monitoring the network activity and account behavior within your AWS environment.

- VPC Flow Logs
- CloudTrail Logs
- DNS Logs
- Optional Features: S3 logs, Lambda network activity, RDS & Aurora login activity.

## WAF

WAF (Web Application Firewall) is a service that can be used to block malicious traffic. It can be used to block malicious traffic, and to block malicious traffic.

- Protects web applications from common web exploits (Layer 7).
- Layer 7 is HTTP (vs Layer 4 is TCP).
- Deploy on Application Load Balancer, API Gateway, CloudFront.

## Network Firewall

- Protect your entire Amazon VPC or segment of a VPC.
- From Layer 3 to Layer 7.

## AWS Certificate Manager (ACM)

- Free service to provision, manage, and deploy SSL/TLS certificates.
- Automatically renew certificates.

## AWS Secrets Manager (ASM)

AWS Secrets Manager is a service that helps you protect secrets needed to access your applications, services, and IT resources. The service enables you to easily rotate, manage, and retrieve database credentials, API keys, and other secrets throughout their lifecycle.

## Inspector

Inspector is an automated security assessment service that helps improve the security and compliance of applications deployed on AWS. Inspector automatically assesses applications for vulnerabilities or deviations from best practices. After performing an assessment, Inspector produces a detailed list of security findings prioritized by level of severity. These findings can be reviewed directly or as part of detailed assessment reports which are available via the Inspector console or API.

**Only for EC2 instances, Container images and Lambda functions.**

- Network accessibility
- Security state of applications

### Macie

Macie is a security service that uses machine learning to automatically discover, classify, and protect sensitive data in AWS. It will alert you to sensitive data in your S3 buckets, such as personally identifiable information (PII) or intellectual property, that has been made publicly available.

### AWS Security Hub

Automatically aggregates alerts in predefined dashboards, or custom dashboards from various AWS services such as GuardDuty, Inspector, Macie, IAM Access Analyzer, Config, IAM Access Analyzer, AWS Systems Manager, and AWS Firewall Manager, AWS Health, and AWS Partner Network (APN) solutions.

### AWS Detective

It is used to find the root cause of security issues or suspicious activities using machine learning and graphs. Automatically collects and process events from AWS GuardDuty, VPC Flow Logs, AWS CloudTrail and create a unified view.

### AWS Abuse

Report suspected AWS resources for abusive or illegal purposes.

examples:

- Spam
- DoS or DDoS

## AWS Security Token Service (STS)

AWS Security Token Service (STS) is a web service that enables you to request temporary, limited-privilege credentials for AWS Identity and Access Management (IAM) users or for users that you authenticate (federated users). The token can then be used to grant access to the AWS resources that are available to the IAM user.

## AWS Cognito

Web and Mobile application users must not have aws accounts to use your apps.

Amazon Cognito is a service that you can use to create unique identities for your users, authenticate these identities with identity providers, and save mobile user data in the AWS Cloud.

## AWS Active Directory Service

AWS Directory Service provides multiple ways to use Amazon Cloud Directory and Microsoft Active Directory (AD) with other AWS services. Directories store information about users, groups, and devices, and administrators use them to manage access to information and resources.

## AWS IAM Identity Center

One login for all AWS accounts in AWS Organizations, business cloud applications(Salesforce, Office 365, etc.), SAML2.0 compliant applications, and EC2 Windows instances.
