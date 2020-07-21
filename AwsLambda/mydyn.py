import json
import boto3

conn = boto3.resource('dynamodb')
table = conn.Table('PlaceOrder')


def lambda_handler(event, context):
    item = {
        'OrderId': int(event['OrderId']),
        'CustomerId': int(event['CustomerId']),
        'PaymentType': event['PaymentType'],
        'OrderType': event['OrderType'],
        'OrderItems': {
            'Item1': event['OrderItems']['Item1'],
            'Item2': event['OrderItems']['Item2']
        },
        'PaymentDetails': {
            'cardnumber': event['PaymentDetails']['cardnumber'],
            'cardname': event['PaymentDetails']['cardname']
        }

    }

    print(type(item))

    response = table.put_item(
        Item=item
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
