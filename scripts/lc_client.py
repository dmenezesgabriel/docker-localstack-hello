import localstack_client.session as session

_session = session.Session()

buckets_client = _session.client("s3")
buckets_list = buckets_client.list_buckets()
print(buckets_list)
sqs_client = _session.client("sqs")
queues_list = sqs_client.list_queues()
print(queues_list)
