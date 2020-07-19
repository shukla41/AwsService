
import boto3
import time
import json
import base64


def insert_data(recList):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('mytab')
    for i in range(len(recList)):
        record = recList[i]
        table.put_item(
            Item={
                'action': record['action'],
                'productId': record['productId']
            }
        )

def lambda_handler(event, context):
    my_stream_name = 'cloudonaut-stream'
    kinesis_client = boto3.client('kinesis', region_name='us-east-1')
    response = kinesis_client.describe_stream(StreamName=my_stream_name)
    my_shard_id = response['StreamDescription']['Shards'][0]['ShardId']
    shard_iterator = kinesis_client.get_shard_iterator(StreamName=my_stream_name,
                                                   ShardId=my_shard_id,
                                                   ShardIteratorType='LATEST')

    my_shard_iterator = shard_iterator['ShardIterator']
    record_response = kinesis_client.get_records(ShardIterator=my_shard_iterator,
                                              Limit=20)
    recList = list()
    for j in record_response:
        record_response = kinesis_client.get_records(ShardIterator=record_response['NextShardIterator'],Limit=2)
        for i in record_response['Records']:
            a = json.loads(i["Data"])
            # record['action']=a['action']
            # record['productId']=a['productId']
            recList.append(a)
            insert_data(recList)
