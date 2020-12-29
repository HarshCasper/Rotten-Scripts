from pgdb import connect
import os
import sys
from awsglue.utils import getResolvedOptions

# CONFIGURATION
redshiftHost = "xyz.redshift.amazonaws.com"
redshiftPort = "5439"
redshiftDatabase = "mydatabase"
redshiftUser = "myadmin"
redshiftPassword = "XYZ"
redshiftSchema = "myschema"
redshifttable = "mytable"
redshiftColumns = "timestamp,value_a,value_b,value_c"
DELIMITER = "\t"
DATEFORMAT = "YYYY-MM-DD"

# ARGUMENTS
args = getResolvedOptions(sys.argv, ["s3-bucket", "s3-object"])
s3Bucket = args["s3_bucket"]
s3Object = args["s3_object"]

con = connect(
    host=redshiftHost + ":" + redshiftPort,
    database=redshiftDatabase,
    user=redshiftUser,
    password=redshiftPassword,
)
cursor = con.cursor()

cursor.execute("set statement_timeout = 360000")

copyQuery = f"COPY {redshiftSchema}.{redshifttable}({redshiftColumns}) from 's3://{s3Bucket}/{s3Object}' iam_role 'arn:aws:iam::111111111111:role/LoadFromS3ToRedshiftJob' delimiter {DELIMITER} DATEFORMAT AS {DATEFORMAT} ROUNDEC TRUNCATECOLUMNS ESCAPE MAXERROR AS 500;"

cursor.execute(copyQuery)
con.commit()
cursor.close()
con.close()
