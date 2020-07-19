import boto3

def lambda_handler(event, context):
    glue = boto3.client('glue')


    myJob = glue.create_job(Name='example_job2', Role='AWSGlueServiceDefaultRole',
                            Command={'Name': 'glueetl','ScriptLocation': 's3://aws-glue-scripts/example_job'},
                            DefaultArguments={"VAL1":"value1","VAL2":"value2","VAL3":"value3"}
                                   )

    glue.start_job_run(JobName=myJob['Name'], Arguments={"VAL1":"value11","VAL2":"value22","VAL3":"value33"})