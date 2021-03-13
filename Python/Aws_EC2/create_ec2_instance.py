import boto3
import os
import datetime

class ec2_instance:
    def __init__(self, ec2Instance: str) -> None:
        self.ec2Instance = ec2Instance

    def key_pair(self):
        
        ec2 = boto3.resource('ec2')

        # create a file to store the key locally
        outfile = open('ec42-keypair.pem','w')

        # call the boto ec2 function to create a key pair
        key_pair = ec2.create_key_pair(KeyName='ec42-keypair')

        # capture the key and store it in a file
        KeyPairOut = str(key_pair.key_material)
        outfile.write(KeyPairOut)


    def create_ec2(self):
        try:
            # create a new EC2 instance
            ec2 = boto3.resource('ec2')
            instances = ec2.create_instances(
                ImageId=self.ec2Instance,
                MinCount=1,
                MaxCount=1,
                InstanceType='t1.micro',
                KeyName='ec42-keypair'
            )
        except Exception as e:
            print(e)
        else:
            print("EC2 Instance created")


if __name__ == "__main__":
    ec2Instance = 'ami-0c7945b4c95c0481c'
    ob= ec2_instance(ec2Instance)
    ob.key_pair()
    ob.create_ec2()
