import json
import boto3
import sys
from botocore.exceptions import ClientError


class secretManagerClass:
    def __init__(self, secretName: str, regionName: str) -> None:
        self.secretName = secretName
        self.regionName = regionName

    def getSecretFromSecretManager(self) -> json:
        session = boto3.session.Session()
        client = session.client(
            service_name="secretsmanager", region_name=self.regionName
        )
        try:
            getSecretValueResponse = client.get_secret_value(SecretId=self.secretName)

        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                print(f"The requested secret {self.secretName} was not found")
                sys.exit(err)
            elif err.response["Error"]["Code"] == "InvalidRequestException":
                print(f"The request was invalid due to: {err}")
                sys.exit(err)
            elif err.response["Error"]["Code"] == "InvalidParameterException":
                print(f"The request had invalid params: {err}")
                sys.exit(err)
        else:
            if "SecretString" in getSecretValueResponse:
                return json.loads(getSecretValueResponse["SecretString"])
            raise ValueError("SecretString not found in reponse")
