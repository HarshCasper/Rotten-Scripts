import os
import sys
import time

# Installation of AWS CLI
install_aws_cli = "pip install awscli"
status = os.system(install_aws_cli)

if status:
    sys.exit("\nError in AWS CLI installation :(\n")
print(
    """\n!! AWS CLI successfully installed !!\n
Get your access keys from IAM Console to configure AWS CLI
You will need to enter following details:
- AWS Access Key ID
- AWS Secret Access Key
- Default region name
- Default output format\n"""
)

time.sleep(10)

# Configuration of AWS CLI
configure_aws = "aws configure"
status = os.system(configure_aws)

if status:
    sys.exit("\nError in AWS Configuration :(\n")
print("\n!! AWS successfully configured !!\n")

# Downloading s3 bucket
bucket_location = input(
    """Enter s3 bucket location using
s3://<bucket>/<path>
format. Example - s3://s3.aws-cli.test/photos/python\n"""
)
download_location = input(
    """Enter location to store downloaded files using
</local/path>
format. Example - ~/Pictures/work/python\n"""
)

download_bucket = "aws s3 sync ".join(bucket_location).join(" ").join(download_location)
status = os.system(download_bucket)

if status:
    sys.exit(
        """\nError in downloading s3 bucket :(
        please provide correct locations\n"""
    )
print("\ns3 bucket successfully downloaded to your desired location\n")
