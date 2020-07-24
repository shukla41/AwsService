import json
import boto3

conn = boto3.resource('dynamodb')
table = conn.Table('PlaceOrder')
'''{
  "OrderId": "1",
  "CustomerId": "1010",
  "PaymentType": "Card",
  "OrderType": "online",
  "OrderItems": {
    "Item1": "pizza",
    "Item2": "bun"
  },
  "PaymentDetails": {
    "cardnumber": 1111,
    "cardname": "visa"
  }
}'''

def lambda_handler(event, context):
    item = {
        'OrderId': int(event['OrderId']),
        'CustomerId': int(event['CustomerId']),
        'PaymentType': event['PaymentType'],
        'OrderType': event['OrderType'],
        'OrderStatus': "Not Confirmed",
        'OrderItems': {
            'Item1': event['OrderItems']['Item1'],
            'Item2': event['OrderItems']['Item2']
        },
        'PaymentDetails': {
            'cardnumber': event['PaymentDetails']['cardnumber'],
            'cardname': event['PaymentDetails']['cardname']
        },
        'PaymentApproved': 'false'

    }

    print(type(item))

    response = table.put_item(
        Item=item
    )

    return {
        'statusCode': 200,
        'body': response
    }
