# AWS Cloud HSM (Hardware Security Module)

## Description

AWS CloudHSM is a cloud-based hardware security module (HSM) that enables you to easily generate and use your own encryption keys on the AWS Cloud. With CloudHSM, you can manage your own encryption keys using FIPS 140-2 Level 3 validated HSMs. It helps you comply with strict security requirements, such as those associated with PCI DSS and HIPAA, and it is generally less expensive than using your own HSMs.

In practice this means that you can use CloudHSM to store your private keys for your SSL certificates. This is a good idea if you want to use the same certificate on multiple servers, or if you want to use the same certificate on a load balancer.
