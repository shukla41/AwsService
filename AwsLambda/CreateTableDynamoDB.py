import boto3

dynamodb = boto3.client("dynamodb")

response = dynamodb.create_table(
  TableName="PlaceOrder",
  AttributeDefinitions=[
    {
      "AttributeName": "OrderId",
      "AttributeType": "N"
    },
    {
      "AttributeName": "CustomerId",
      "AttributeType": "N"
    }
  ],
  KeySchema=[
    {
      "AttributeName": "OrderId",
      "KeyType": "HASH"
    },
    {
      "AttributeName": "CustomerId",
      "KeyType": "RANGE"
    }
  ],
  ProvisionedThroughput={
    "ReadCapacityUnits": 1,
    "WriteCapacityUnits": 1
  }
)

print(response)