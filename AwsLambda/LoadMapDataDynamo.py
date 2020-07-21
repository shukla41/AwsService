import boto3
import json

dynamodb = boto3.client('dynamodb')

def upload():
    with open('C:\\Users\\shumondal\\PycharmProjects\\Lambda\\resource\\data.json', 'r') as datafile:
        records = json.load(datafile)
        for song in records:
            print(song)
            item = {
                'artist': {'S': song['artist']},
                'song': {'S': song['song']},
                'id': {'S': song['id']},
                'info':{'M': {
                'priceUsdCents': {'S': str(song['priceUsdCents'])},
                'publisher': {'S': song['publisher']}
                }
               }}

            print(item)
            response = dynamodb.put_item(
                TableName='PlaceOrder24',
                Item=item
            )
            print("UPLOADING ITEM")
            print(response)


upload()

{'OrderId': {'N': '1'}, 'CustomerId': {'N': '1010'}, 'PaymentType': {'S': 'Card'}, 'OrderType': {'S': 'online'}, 'OrderItems': {'M': {'Item1': {'S': 'pizza'}, 'Item2': {'S': 'bun'}}}, 'PaymentDetails': {'M': {'cardnumber': {'S': 1111}, 'cardname': {'S': 'visa'}}}}