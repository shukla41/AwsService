import json


def lambda_handler(event, context):
    OrderId = event['OrderId']

    tempStr = 'Order ' + OrderId + ': is not delivered due to transaction..cardnumber  not match'
    response = {
        'Order': OrderId,
        'Message': tempStr
    }

    return response