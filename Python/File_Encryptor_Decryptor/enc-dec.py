import os
import sys
import getopt
from pwinput import pwinput
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

# --- SET DEFAULTS ---
is_encrypt = False
is_decrypt = False
org_file_name = ''
argumentList = sys.argv[1:]
options = 'e:d:'

# --- DEFINE ARG OPERATIONS ---
try:
    args, values = getopt.getopt(argumentList, options)
    for currentArgument, currentValue in args:
        if currentArgument in ('-e'):
            is_encrypt = True
            org_file_name = currentValue
            print('Encrypt :', currentValue)
        if currentArgument in ('-d'):
            is_decrypt = True
            org_file_name = currentValue
            print('Decrypt :', currentValue)
except getopt.error as e:
    print(str(e))

# --- FUNCTION FOR ENCRYPTION ---
def encrypt(key, filename):
    chunksize = 64*1024
    outputFile = "encrypted/enc-"+filename
    filesize = str(os.path.getsize('original/'+filename)).zfill(16)
    IV = Random.new().read(16)
    encryptor = AES.new(key, AES.MODE_CBC, IV)
    
    with open('original/'+filename, 'rb') as infile:
        with open(outputFile, 'wb') as outfile:
            outfile.write(filesize.encode('utf-8'))
            outfile.write(IV)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - (len(chunk) % 16))
                outfile.write(encryptor.encrypt(chunk))

# --- FUNCTION FOR DECRYPTION ---
def decrypt(key, filename):
    chunksize = 64*1024
    outputFile = "decrypted/dec-"+filename[4:]

    with open('encrypted/'+filename, 'rb') as infile:
        filesize = int(infile.read(16))
        IV = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, IV)
        with open(outputFile, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(filesize)

# --- PASSWORD HASHING ---
def getKey(password):
    hasher = SHA256.new(password.encode('utf-8'))
    return hasher.digest()

def Main():

    # --- ENCRYPT OPTION SELECTED ---
    if is_encrypt:
        filename = org_file_name
        password = pwinput(prompt='Encryption Password : ')
        encrypt(getKey(password), filename)
        print('Encryption Done! Encrypted file in "encrypted" folder.')

    # --- DECRYPT OPTION SELECTED ---
    elif is_decrypt:
        filename = org_file_name
        password = pwinput(prompt='Decryption Password : ')
        decrypt(getKey(password), filename)
        print('Decryption Done! Decrypted file in "decrypted" folder.')

    # --- INVALID OPTIONS PASSED ---
    else:
        print('Invalid Option! Closing...')

if __name__ == '__main__':
    Main()