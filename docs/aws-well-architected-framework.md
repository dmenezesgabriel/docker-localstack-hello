# AWS Well Architected Framework

## Description

The AWS Well-Architected Framework helps you understand the pros and cons of decisions you make while building systems on AWS. By using the Framework you will learn architectural best practices for designing and operating reliable, secure, efficient, and cost-effective systems in the cloud. It provides a way for you to consistently measure your architectures against best practices and identify areas for improvement.

### General guiding principles

- Stop guessing your capacity needs
- Test systems at production scale
- Automate to make architectural experimentation easier
- Allow for evolutionary architectures
- Drive architectures using data
- Improve through game days

### Design Principles

- Scalability: vertical & horizontal
- Disposable resources: servers should be disposable & easily configurable
- Automation: Serverless, Infrastructure as a Service, Auto Scaling, ...
- Loose Coupling: Services should be loosely coupled
- Services, not Servers: Use managed services instead of managing your own servers

## Pillars

- [Operational Excellence](aws-well-architected-framework.md#operational-excellence)
- [Security](aws-well-architected-framework.md#security)
- [Reliability](aws-well-architected-framework.md#reliability)
- [Performance Efficiency](aws-well-architected-framework.md#performance-efficiency)
- [Cost Optimization](aws-well-architected-framework.md#cost-optimization)
- [Susteinability](aws-well-architected-framework.md#sustainability)

### Operational Excellence

Operational excellence is the ability to run and monitor systems to deliver business value and continually improve supporting processes and procedures.

Design Principles:

- Perform operations as code
- Annotate documentation
- Make frequent, small, reversible changes
- Refine operations procedures frequently
- Anticipate failure

### Security

Security is the ability to protect information, systems, and assets while delivering business value through risk assessments and mitigation strategies.

### Reliability

Reliability is the ability of a system to recover from infrastructure or service disruptions, dynamically acquire computing resources to meet demand, and mitigate disruptions such as misconfigurations or transient network issues.

### Performance Efficiency

Performance efficiency is the ability to use computing resources efficiently to meet system requirements, and to maintain that efficiency as demand changes and technologies evolve.

### Cost Optimization

Cost optimization is the ability to run systems to deliver business value at the lowest price point.

### Sustainability

Sustainability is the ability to design, deploy, and operate systems that deliver business value and continue to meet requirements as the business evolves.

## AWS Well-Architected Tool

The AWS Well-Architected Tool is a service in the cloud that provides a consistent process for you to review and measure your architecture using the AWS Well-Architected Framework. The tool is based on AWS best practices for building and deploying reliable, secure, efficient, and cost-effective systems in the cloud. It provides a set of questions that allows you to review an existing or proposed architecture. The tool then provides a plan with guidance on improving the architecture.
