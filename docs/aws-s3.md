# S3 - Simple Storage Service

## Description

- Storage any type of files (5 Terabytes for file)
- Unlimited storage (Charged per Gigabyte)
- Create Buckets (similar to hd partitions) with folders inside.

## Features

- Versioning
- Encryption
- ACL

## Components

Object Base

- Key: File name
- Value: File content
- Version: File version (If enabled)
- Metadata: Tag, local, etc
- ACL

## Tiers

- S3 Standard: Replicated for at least 2 availability zones, with 99.99% of availability and durability.
- S3 IA (Infrequent Access): Cheaper, but with a access fee, replicated for at least 2 availability zones.
- S3 One Zone: Similar with IA but with one availability zone.
- Glacier: For backup purposes, it takes from 3 to 5 hours to retrieve a file.

## Charges

- Storage: Per Gigabyte
- Request: Per Access
- Storage management price (Tags, Versioning)
- DTP (Data Transfer Pricing): Transfer between regions.
- Transfer Acceleration: CDN, CloudFront
