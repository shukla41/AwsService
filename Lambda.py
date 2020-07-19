import json, boto3
client = boto3.client('lambda')
response = client.create_function(
    FunctionName='KinesisLam',
    Runtime='python3.6',
    Role='arn:aws:iam::246939968246:role/myrole',
    Handler='KinesisLam.lambda_handler',
    Code= {'ZipFile': open(r'C:\Users\shumondal\PycharmProjects\Lambda\mylambda.zip', 'rb').read() })
