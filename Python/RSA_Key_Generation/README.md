# Generate Public Keys
## This script is used to create a private/public keypair for SSH-authentication for password-less connecting to a remote server.

+ On running this script, will create two files with (.pem) format which contains public and private key.
+ Defined length of keys are 4096 bits *(recommended size)* which determines the strength of keys.

## To run the script:
1. Install the dependencies by running following command in terminal.

   `pip install pycryptodome`

2. Run the script.

    `python RSA.py`

    The script runs until you enter valid commands- 
    1) generate_keys \<folder path to store keys\>
    
     \(eg - `generate_keys ./keys`\)

    2) encrypt \<path to public key file\> \<file to encrypt\> \<encrypted file name\> 
    
     \(eg - `encrypt ./keys/public_key.pem nature.jpeg enc_script`\)

    3) decrypt \<path to private key file\> \<file to decrypt\> \<decrypted file name\> 
    
     \(eg - `decrypt ./keys/private_key.pem enc_script NATURE.jpeg` \)

    4) exit- to exit from the program  
    
     \(eg - `exit`\)
    
In case, if you want to know more, Read complete documentation [here](https://pycryptodome.readthedocs.io/en/latest/src/public_key/rsa.html)
    
