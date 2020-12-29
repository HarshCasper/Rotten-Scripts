# Load data from S3 to Redshift

The code example executes the following steps:

1. import modules that are bundled by AWS Glue by default.
2. Define some configuration parameters (e.g., the Redshift hostname RedshiftHOST).
3. Read the S3 bucket and object from the arguments (see getResolvedOptions) handed over when starting the job.
4. Establish a connection to Redshift: connect(...).
5. Increase the statement timeout (see statement_timeout) to one hour.
6. Execute the COPY query to tell Redshift to the object from S3.