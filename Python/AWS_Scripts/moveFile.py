import boto3

awsAccessKeyId = ""
awsSecretAccessKey = ""
bucketName = ""
directoryName = ""
s3 = boto3.resource(
    's3',
    aws_access_key_id=awsAccessKeyId,
    aws_secret_access_key=awsSecretAccessKey
)
myBucket = s3.Bucket(bucketName)


def moveFile():
    try:
        for objectSummary in myBucket.objects.filter(Prefix=directoryName):
            s3FilePath = objectSummary.key
            sourceFilename = (s3FilePath).split("/")[-1]
            copySource = {"Bucket": bucketName, "Key": s3FilePath}
            targetFilename = f"{destinationDirectory}/{sourceFilename}"
            s3.meta.client.copy(copySource, bucketName, targetFilename)
            s3.Object(bucketName, s3FilePath).delete()
    except Exception as err:
        print(err)


if __name__ == '__main__':
    moveFile()
