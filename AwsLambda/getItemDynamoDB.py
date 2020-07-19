import boto3
import json
from boto3.dynamodb.conditions import Key,Attr

dynamodb = boto3.client('dynamodb')
response = dynamodb.get_item(TableName='basictab1',
    Key={
        'artist': {'S': 'Arturus Ardvarkian'},
        'song': {'S': 'Baker Firebrick'}
    }
)
print(response)

response1 = dynamodb.query(
    TableName='basictab1',
    KeyConditionExpression='artist = :artist AND begins_with ( song , :song )',
    ExpressionAttributeValues={
        ':artist': {'S': 'Arturus Ardvarkian'},
        ':song': {'S': 'C'}
    }
)

print(response1['Items'])

response2 = dynamodb.get_item(
    TableName='basictab1',
    Key={
        'artist': {'S': 'Arturus Ardvarkian'},
        'song': {'S': 'Baker Firebrick'}
    },

    ProjectionExpression='info'
)

print(response2['Item']['info']['M']['priceUsdCents']['S'])


response3 = dynamodb.update_item(
    TableName='basictab1',
    Key={
        'artist': {'S': 'Arturus Ardvarkian'},
        'song': {'S': 'Baker Firebrick'}
     },
    AttributeUpdates={
        'info': {
            'Value':  {'M': {
                    'priceUsdCents': {'S':'455'}
                }
        }}
    }
  )

print(response3)