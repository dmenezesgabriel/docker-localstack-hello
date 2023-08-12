# Billing and Pricing

- Pay as you go. No upfront costs. No termination fees.
- Pay for what you use.
- Pay less to use more.
- Pay even less when you reserve.

## Description

AWS Billing and Cost Management is the service that you use to pay your AWS bill, monitor your usage, and analyze and control your costs.

## CAPEX & OPEX

- Capital Expenditure (CAPEX): Upfront payment to buy a physical server, and then pay for maintenance. Ex: reserved instances.
- Operational Expenditure (OPEX): Pay for what you use. Ex: on-demand instances.

## Pricing Calculator

> Create an estimate for the cost of your use cases on AWS.

- [Pricing Calculator](https://calculator.aws/#/)

Pricing Calculator lets you explore AWS services, and create an estimate for the cost of your use cases on AWS.

## Services

- [Lambda](aws-lambda.md#pricing)
- [EC2](aws-ec2.md#pricing)
- [S3](aws-s3.md#pricing)

## Billing Dashboard

- [Billing Dashboard](https://console.aws.amazon.com/billing/home?#/dashboard)

The Billing and Cost Management Dashboard displays the current status of your bill and payment settings based on your account activity. You can view your current month-to-date costs, forecast how much you are likely to spend by the end of the month, and get recommendations for how to optimize your costs.

## Consolidate Billing

> Combine usage across accounts to receive volume pricing discounts.

- [Consolidate Billing](https://console.aws.amazon.com/billing/home?#/account)

Consolidated billing enables you to consolidate payment for multiple AWS accounts within your company by designating a single paying account. Consolidated billing is offered at no additional charge.

### Benefits

- Bulk discounts for all accounts.
- Volume discounts for all accounts.
- All accounts under a single bill.
- All accounts under a single payment method.
- All accounts under a single support plan.

## Budgets

> Review how much cost your predicted AWS usage will incur by the end of the month.

- [Budgets](https://console.aws.amazon.com/billing/home?#/budgets)

Budgets give you the ability to set custom budgets that alert you when your costs or usage exceed (or are forecasted to exceed) your budgeted amount.

- You can also use AWS Budgets to set reservation utilization or coverage targets and receive alerts when your utilization drops below the threshold you define. Reservation alerts are supported for Amazon EC2, Amazon RDS, Amazon Redshift, Amazon ElastiCache, and Amazon Elasticsearch reservations.

## Cost Explorer

> Visualize and manage your AWS costs and usage **over time**.

- [Cost Explorer](https://console.aws.amazon.com/billing/home?#/costexplorer)

Cost Explorer has an easy-to-use interface that lets you visualize, understand, and manage your AWS costs and usage over time.

- Forecast future costs and usage.
- Rightsizing recommendation feature to help identify underutilized EC2 instances across member accounts.

## Billing Alarm

Available only in the `us-east-1` region.

## Compute Savings Plans

Reduce your compute costs by committing to a consistent amount of compute usage (measured in $/hour) for a 1 or 3 year term.

## AWS Compute Optimizer

Analyze your compute usage patterns to identify opportunities to save money.

It applies to:

- EC2
- EBS Volume configurations
- Auto Scaling Groups
- Lambda functions

## Cost Allocation Tax

Tag your AWS resources to easily identify their cost on your bill.

## Cost and Usage Report

Access comprehensive cost and usage information as a CSV or Parquet file.

## AWS Anomaly Detection

Continuously monitors your usage and cost trends to identify unusual spending patterns using Machine Learning.

## AWS Service Quotas

Create CloudWatch alarms to notify you when you are approaching your service quotas.

- Example: EC2 instances per region, Lambda concurrent executions, etc.

## Reservation to optimize costs

- EC2
- DynamoDB
- RDS
- ElastiCache
- Redshift
