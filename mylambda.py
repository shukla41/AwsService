import boto3
s3 = boto3.resource('s3')
def lambda_handler(event, context):
    copy_source = {
        'Bucket': 'source-buc2',
        'Key': 'Ec2.yaml'
    }
    s3.meta.client.copy(copy_source, 'target-buc2','Ec2.yaml')