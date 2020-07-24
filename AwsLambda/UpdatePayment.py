import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('PlaceOrder')


def lambda_handler(event, context):
    print('my even', event)

    response = table.get_item(
        Key={
            'OrderId': int(event['OrderId']),
            'CustomerId': int(event['CustomerId'])
        },

        ProjectionExpression='PaymentDetails'
    )

    # print(response['Item']['PaymentDetails']['cardnumber'])

    if (event['PaymentDetails']['cardnumber'] == response['Item']['PaymentDetails']['cardnumber']):
        response3 = table.update_item(
            TableName='PlaceOrder',
            Key={
                'OrderId': int(event['OrderId']),
                'CustomerId': int(event['CustomerId'])
            },
            AttributeUpdates={
                'OrderStatus': {'Value': 'Confirmed'}
            }
        )
        chk = {"paymentSuccess": "true"}
    else:
        chk = {"paymentSuccess": "false"}

    return {
        'statusCode': 200,
        'body': chk
    }
