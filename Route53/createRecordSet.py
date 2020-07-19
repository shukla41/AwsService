import boto3

client = boto3.client('route53')
response = client.change_resource_record_sets(
    HostedZoneId='Z07575521OTTNHJJ0KYQB',
    ChangeBatch={
        'Comment': 'string',
        'Changes': [
            {
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'Name': 'www.cmcloudlab1404.info.',
                    'Type': 'A',
                    'TTL': 123,
                    'ResourceRecords': [
                        {
                            'Value': '34.200.220.130'
                        },
                        {
                            'Value': '54.174.206.95'
                        },
                    ],
                }
            },
        ]
    }
)