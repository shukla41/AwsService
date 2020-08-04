import json


def lambda_handler(event, context):
    print('Function loaded successfully');
    paymentSuccess = event['paymentSuccess']
    OrderId = event['OrderId']

    tempStr = 'Order ' + str(paymentSuccess) + ': Order is being delivered...'
    response = {
        'Order': OrderId,
        'Message': tempStr
    }

    return response