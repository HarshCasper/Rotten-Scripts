import sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import zlib
import base64
from keyPair_generation import keyPairGeneration
from utilities import Utilities


class RSA_algorithm:
    def encrypt(self, public_key, blob):
        #Import the Public Key and use for encryption using PKCS1_OAEP
        rsa_key = RSA.importKey(public_key)
        rsa_key = PKCS1_OAEP.new(rsa_key)

        #compress the data first
        blob = zlib.compress(blob)

        '''In determining the chunk size, determine the private key length used in bytes and subtract 42 bytes 
        (when using PKCS1_OAEP). The data will be in encrypted in chunks'''
        chunk_size = 470
        offset = 0
        end_loop = False
        encrypted =  b''

        while not end_loop:
            #The chunk
            chunk = blob[offset:offset + chunk_size]

            #If the data chunk is less then the chunk size, then we need to add
            #padding with " ". This indicates the we reached the end of the file
            #so we end loop here
            if len(chunk) % chunk_size != 0:
                end_loop = True
                chunk += b'' * (chunk_size - len(chunk))

            #Append the encrypted chunk to the overall encrypted file
            encrypted += rsa_key.encrypt(chunk)

            #Increase the offset by chunk size
            offset += chunk_size

        #Base 64 encode the encrypted file
        return base64.b64encode(encrypted)

    def decrypt(self, private_key, encrypted_blob):
        #Import the Private Key and use for decryption using PKCS1_OAEP
        rsakey = RSA.importKey(private_key)
        rsakey = PKCS1_OAEP.new(rsakey)

        #Base 64 decode the data
        encrypted_blob = base64.b64decode(encrypted_blob)

        #In determining the chunk size, determine the private key length used in bytes.
        #The data will be in decrypted in chunks
        chunk_size = 512
        offset = 0
        decrypted = b''

        #keep loop going as long as we have chunks to decrypt
        while offset < len(encrypted_blob):
            #The chunk
            chunk = encrypted_blob[offset: offset + chunk_size]

            #Append the decrypted chunk to the overall decrypted file
            decrypted += rsakey.decrypt(chunk)

            #Increase the offset by chunk size
            offset += chunk_size

        #return the decompressed decrypted data
        return zlib.decompress(decrypted)



if __name__ == '__main__':
    while True:
        command= input().strip().split(' ')

        # if the user demands to generate the key pair
        if command[0] == 'generate_keys':
            try:
                filePath_for_Keys= command[1]
                kpg= keyPairGeneration(filePath_for_Keys)
            except:
                print ("Please verify the file path(s) given.")

        # if the user demands to encrypt some confidential file
        elif command[0] == 'encrypt':
            try:
                # extract the path of the public key file
                filePath_of_PublicKey= command[1]
                # extract the path of the file to be encrypted
                file_to_encrypt= command[2]
                # extract the filename user demands to give to will be formed encrypted file
                encrypted_filename= command[3]

                # creating object of utilities to access
                util= Utilities()

                # read the public key
                publicKey= util.readFile(filePath_of_PublicKey)
                # read the to be encrypted content
                unencrypted_blob= util.readFile(file_to_encrypt)

                rsa= RSA_algorithm()
                # encrypt the content
                encrypted_blob= rsa.encrypt(publicKey, unencrypted_blob)
                # write the encrypted blob to get the encrypted contents of the file
                util.writeFile(encrypted_filename, encrypted_blob)

            except:
                print ("Please verify the file path(s) given.")

        # if the user demands to decrypt some encrypted file
        elif command[0] == 'decrypt':
            try:
                # extract the path of the private key file
                filePath_of_PrivateKey= command[1]
                # extract the path of the file to be decrypted
                file_to_decrypt= command[2]
                # extract the filename user demands to give to will be formed decrypted file
                decrypted_filename= command[3]

                # creating object of utilities to access
                util= Utilities()

                # read the private key
                privateKey= util.readFile(filePath_of_PrivateKey)
                # read the to be decrypted content
                encrypted_blob= util.readFile(file_to_decrypt)

                rsa= RSA_algorithm()
                # decrypt the content
                decrypted_blob= rsa.decrypt(privateKey, encrypted_blob)
                # write the decrypted blob to get the original contents of file
                util.writeFile(decrypted_filename, decrypted_blob)

            except:
                print ("Please verify the file path(s) given.")

        # user demads to exit from the program
        elif command[0] == 'exit':
            break

        else:
            print ("Invalid Command, please verify from the manual.")
