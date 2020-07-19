import json
import boto3

conn= boto3.resource('dynamodb')
table=conn.Table('planet')

'''
{
  "id": "moon",
  "temp": "so cold"
}
// if you use map in dynamodb , input will be to insert
{
  "id": 3,
  "item": 
    {
        "itemnumber": "3",
         "prd": "laptop"
        
    }
}

'''
def lambda_handler(event, context):
    print('my even',event['id'])
    response=table.get_item(
        Key={'id': 'earth'}
    )
    print(response)
    write=table.put_item(
        Item=event
    )
    return {
        'statusCode': 200,
        'body': response ,
        'body' :write
    }