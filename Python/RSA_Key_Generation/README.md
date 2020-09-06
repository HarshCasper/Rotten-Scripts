# Generate Public Keys
## This script is used to create a private/public keypair for SSH-authentication for password-less connecting to a remote server.

+ On running this script, will create two files with (.pem) format which contains public and private key.
+ Defined length of keys are 2048 bits *(recommended size)* which determines the strength of keys.

## To run the script:
1. Install the dependencies by running following command in terminal.
    + pip install pycryptodome
2. Run the script.
    + python rsa_key_generation.py
    
In case, if you want to know more, Read complete documentation [here](https://pycryptodome.readthedocs.io/en/latest/src/public_key/rsa.html)
    
