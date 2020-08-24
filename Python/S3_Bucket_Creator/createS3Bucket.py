import boto3
import os
import datetime


class s3Bucket:
    def __init__(self, bucketName: str) -> None:
        self.bucketName = bucketName

    def createS3Bucket(self):
        try:
            client = boto3.client("s3")
            client.create_bucket(
                ACL="private",
                Bucket=self.bucketName,
                CreateBucketConfiguration={"LocationConstraint": "us-west-1"},
            )
        except Exception as err:
            print(err)
        else:
            print("S3 bucket creation Successful!")


if __name__ == "__main__":
    date = datetime.datetime.now()
    current_time = "{}{}{}".format(date.month, date.day, date.year)
    bucketName = "yourName{}".format(current_time)
    obj = s3Bucket(bucketName)
    obj.createS3Bucket()
