# How do I create an EC2 Instance?

Before we can get started, you'll need to install `Boto3` library in Python and the AWS Command Line Interface (CLI) tool using `pip` which is a package management system written in Python used to install and manage packages that can contain code libraries and dependent files.

Boto3 is the AWS SDK for Python, which provides Object-based APIs and low-level direct access to AWS services like EC2. AWS CLI is a command line tool written in Python that introduces efficient use cases to manage AWS services with a set of very simple commands.

Using 'pip' run the following command to install the AWS CLI and Python's Boto3 library on your machine:

`pip install awscli boto3`

## AWS Configure to Config AWS Creds

After creating the user and obtaining the credentials (Access ID and Secret key), we can now configure our Python scripting environment with this credential in order to manage EC2.

Use the AWS CI tool to configure these credentials by running the following command from a Bash terminal:

`aws configure`

It will prompt you to provide the Access Key ID, Secret Key, Default AWS region, and output format. Once those are provided, credentials are saved in a local file at path *~/.aws/credentials* and other configurations like region are stored in *~/.aws/config* file.

## Create Key Pair for EC2 Instance

Before we can jump into how to create EC2 instances, it's important to understand how to create a keypair for EC2 instances, so that they can be accessed later, once the virtual machines are launched programmatically using Python.

## Create a New EC2 Instance

Now that we've configured our credentials, let's test if these credentials work well with AWS CLI tools. To do that, run the following command from a Bash shell:

`aws ec2 describe-instances`

In the above output you can see the Amazon Machine Image (AMI) ID, which looks like ami-00b6a8a2bd28daf19, this is important information, and is required to create a new instance programmatically using Python.
