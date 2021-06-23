# ch9_generate_keys.py
from Crypto.PublicKey import RSA
from utilities import Utilities


class keyPairGeneration:
    def __init__(self, filePath):
        # Generate a public/ private key pair using 4096 bits key length (512 bytes)
        new_key = RSA.generate(4096, e=65537)

        # creating object of utilities to access
        util = Utilities()

        # The private key in PEM format
        private_key = new_key.exportKey("PEM")
        # write the private key
        util.writeFile(filePath + "/private_key.pem", private_key)

        # The public key in PEM Format
        public_key = new_key.publickey().exportKey("PEM")
        # write the public key
        util.writeFile(filePath + "/public_key.pem", public_key)
