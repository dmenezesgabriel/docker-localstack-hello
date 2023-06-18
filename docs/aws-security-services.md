# Security Services

## Inspector

Inspector is an automated security assessment service that helps improve the security and compliance of applications deployed on AWS. Inspector automatically assesses applications for vulnerabilities or deviations from best practices. After performing an assessment, Inspector produces a detailed list of security findings prioritized by level of severity. These findings can be reviewed directly or as part of detailed assessment reports which are available via the Inspector console or API.

## Trusted Advisor

- [Checks](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor-check-reference.html)

Trusted Advisor is an online resource to help you reduce cost, increase performance, and improve security by optimizing your AWS environment. Trusted Advisor provides real time guidance to help you provision your resources following AWS best practices.

Examples of checks:

- MFA on root account
- S3 bucket permissions

## CloudTrail

CloudTrail is a web service that records AWS API calls for your account and delivers log files to you. The recorded information includes the identity of the API caller, the time of the API call, the source IP address of the API caller, the request parameters, and the response elements returned by the AWS service.

## Athena vs Macie

- Athena: Query data in S3.
- Macie: Discover and protect sensitive data.

### Macie

Macie is a security service that uses machine learning to automatically discover, classify, and protect sensitive data in AWS. Macie recognizes sensitive data such as personally identifiable information (PII) or intellectual property, and provides you with dashboards and alerts that give visibility into how this data is being accessed or moved. Macie continuously monitors data access activity for anomalies, and generates detailed alerts when it detects risk of unauthorized access or inadvertent data leaks. Macie works by using a combination of machine learning, natural language processing, and pattern matching to understand the content and context of files stored in Amazon S3. It uses this understanding to assign each file a business value, and then continuously monitors the file in order to detect any suspicious activity associated with the file.
It is most used by security analysts, data analysts, and compliance officers.
