How do I create an S3 Bucket?
=============================

|checkout|

Before you can upload data to Amazon S3, you must create a bucket in one
of the AWS Regions to store your data. After you create a bucket, you
can upload an unlimited number of data objects to the bucket.

The AWS account that creates the bucket owns it. By default, you can
create up to 100 buckets in each of your AWS accounts. If you need
additional buckets, you can increase your account bucket quota to a
maximum of 1,000 buckets by submitting a service quota increase. For
information about how to increase your bucket quota, see AWS Service
Quotas in the AWS General Reference.

To create a bucket using python
-------------------------------

1. Install boto3 library

A low-level client representing Amazon Simple Storage Service (S3):

2. The following operations are related to CreateBucket :

PutObject DeleteBucket

See also:
`Documentation <https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html>`__

Examples

The following example creates a bucket. The request specifies an AWS
region where to create the bucket.

``import boto3``

``client = boto3.client('s3')``

``response = client.create_bucket(     Bucket='examplebucket',     CreateBucketConfiguration={         'LocationConstraint': 'eu-west-1',     } )``

.. |checkout| image:: https://forthebadge.com/images/badges/check-it-out.svg
  :target: https://github.com/HarshCasper/Rotten-Scripts/tree/master/Python/S3_Bucket_Creator/

