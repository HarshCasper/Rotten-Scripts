AWS Secrets Manager
===================

|checkout|

This Python example shows you how to retrieve the decrypted secret value
from an AWS Secrets Manager secret. The secret could be created using
either the Secrets Manager console or the CLI/SDK.

The code uses the AWS SDK for Python to retrieve a decrypted secret
value.

Prerequisite tasks
------------------

To set up and run this example, you must first set up the following:

1. Configure your AWS credentials, as described in `Quickstart <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html>`__.
2. Create a secret with the AWS Secrets Manager, as described in the `AWS Secrets Manager Developer Guide <https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_create-basic-secret.html>`__

Retrieve the secret value
=========================

The following example shows how to:

1. Retrieve a secret value using ``get_secret_value``.

.. |checkout| image:: https://forthebadge.com/images/badges/check-it-out.svg
  :target: https://github.com/HarshCasper/Rotten-Scripts/tree/master/Python/AWS_Scripts/

