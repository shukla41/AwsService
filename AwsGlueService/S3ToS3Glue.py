import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
data = spark.read.csv("s3://aniya111/Corn-US.csv")
f = DynamicFrame.fromDF(data,
                        glueContext,
                        "convert_ctx"
                        )

'''glueContext.write_dynamic_frame.from_options(
    frame=f,
    connction_type="S3",
    connection_options = {"path": "s3://aniya222/"},
    format = "csv",
    transformation_ctx = "transformation_ctx")'''

glueContext.write_dynamic_frame.from_options(
    frame = f,
    connection_type = "s3",
    connection_options = {
        "path": "s3://aniya222/",
    },
    format = "csv"
)
job.commit()