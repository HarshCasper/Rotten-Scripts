import os
import sys
import getopt
from pwinput import pwinput
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

# --- FUNCTION FOR ENCRYPTION ---
def encrypt(key, filename):
    chunksize = 64*1024
    output_file = "encrypted/enc-"+filename
    filesize = str(os.path.getsize('original/'+filename)).zfill(16)
    iv_value = Random.new().read(16)
    encryptor = AES.new(key, AES.MODE_CBC, iv_value)

    with open('original/'+filename, 'rb') as infile, open(output_file, 'wb') as outfile:
        outfile.write(filesize.encode('utf-8'))
        outfile.write(iv_value)
        while True:
            chunk = infile.read(chunksize)
            if len(chunk) % 16 != 0:
                chunk += b' ' * (16 - (len(chunk) % 16))
            elif len(chunk) == 0:
                break
            outfile.write(encryptor.encrypt(chunk))

# --- FUNCTION FOR DECRYPTION ---
def decrypt(key, filename):
    chunksize = 64*1024
    output_file = "decrypted/dec-"+filename[4:]

    with open('encrypted/'+filename, 'rb') as infile, open(output_file, 'wb') as outfile:
        filesize = int(infile.read(16))
        iv_value = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv_value)
        while True:
            chunk = infile.read(chunksize)  
            if len(chunk) == 0:
                break
            outfile.write(decryptor.decrypt(chunk))
        outfile.truncate(filesize)

# --- PASSWORD HASHING ---
def get_key(password):
    hasher = SHA256.new(password.encode('utf-8'))
    return hasher.digest()

def Main():

    # --- SET DEFAULTS ---
    is_encrypt = False
    is_decrypt = False
    org_file_name = ''
    argument_list = sys.argv[1:]
    options = 'e:d:'

    # --- DEFINE ARG OPERATIONS ---
    try:
        args, _ = getopt.getopt(argument_list, options)
        for current_argument, current_value in args:
            if current_argument in ('-e'):
                is_encrypt = True
                org_file_name = current_value
                print('Encrypt :', current_value)
            if current_argument in ('-d'):
                is_decrypt = True
                org_file_name = current_value
                print('Decrypt :', current_value)
    except getopt.error as error:
        print(str(error))

    # --- ENCRYPT OPTION SELECTED ---
    if is_encrypt:
        filename = org_file_name
        password = pwinput(prompt='Encryption Password : ')
        encrypt(get_key(password), filename)
        print('Encryption Done! Encrypted file in "encrypted" folder.')

    # --- DECRYPT OPTION SELECTED ---
    elif is_decrypt:
        filename = org_file_name
        password = pwinput(prompt='Decryption Password : ')
        decrypt(get_key(password), filename)
        print('Decryption Done! Decrypted file in "decrypted" folder.')

    # --- INVALID OPTIONS PASSED ---
    else:
        print('Invalid Option! Closing...')

if __name__ == '__main__':
    Main()
