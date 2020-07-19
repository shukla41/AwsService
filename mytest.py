import json
import base64
import boto3

recList = list()


def lambda_handler(event, context):
    for record in event['Records']:
        # payload=base64.b64decode(record["kinesis"]["data"]).decode('utf8')
        payload = json.loads(base64.b64decode(record['kinesis']['data']))
        print(payload)
        recList.append(payload)
        insert_data(recList)

    return {
        'statusCode': 200,
        'body': json.dumps('Loaded!')
    }


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