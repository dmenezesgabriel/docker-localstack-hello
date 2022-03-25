import localstack_client.session

session = localstack_client.session.Session()

buckets_client = session.client("s3")
buckets_list = buckets_client.list_buckets()
print(buckets_list)
sqs_client = session.client("sqs")
queues_list = sqs_client.list_queues()
print(queues_list)
