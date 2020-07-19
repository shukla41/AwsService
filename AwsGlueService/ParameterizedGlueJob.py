import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
args = getResolvedOptions(sys.argv, ['JOB_NAME','VAL1','VAL2','VAL3','DEST_FOLDER'])
job.init(args['JOB_NAME'], args)

v_list=[{"VAL1":args['VAL1'],"VAL2":args['VAL2'],"VAL3":args['VAL3']}]

df=sc.parallelize(v_list).toDF()
df.repartition(1).write.mode('overwrite').format('csv').options(header=True, delimiter = ';').save("s3://"+ args['DEST_FOLDER'] +"/")

job.commit()