# Static Site S3

## Steps

1. Deploy localstack

docker-compose up localstack

2. Create bucket

```sh
awslocal s3api create-bucket --bucket static-site-bucket
```

3. Verify buckets

```sh
awslocal s3 ls
```

4. Copy file to bucket

```sh
awslocal s3 sync ./samples/static_site_s3 s3://static-site-bucket --acl public-read
```

5. Copy file to bucket

```sh
awslocal s3 website s3://static-site-bucket --index-document public/index.html
```

5. Access the site.

http://static-site-bucket.s3-website.localhost.localstack.cloud:4566/
