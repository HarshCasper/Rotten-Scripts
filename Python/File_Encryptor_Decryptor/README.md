## File Encryption and Decryption :

### Description :
- The script lets you encrypt or decrypt a file.
- To do so, we use the [pycryptodome](https://pycryptodome.readthedocs.io/en/latest/) library.
- The user passes the function and also the file on which the same is to be performed.
- Once the parameters are passed, the encryptor needs to specify a password which is later required on the decryptor's side to decrypt the file.
- All passwords are hidden with asteriks using the [pwinput](https://github.com/asweigart/pwinput) library.

### Try it out yourself :

- Install libraries : ```pip install -r requirements.txt```
- The parameters that are to be passed are :
    * Operation : ```-e/-d``` for encryption/decryption [any one]
    * File name : pass ```filename.ext``` after operation
- Place your file in the "original" folder.
- Once file.txt is encrypted, a new encrypted file called enc-file.txt is generated in the "encrypted" folder.
- The encrypted file enc-file.txt when decrypted, results in a new file called dec-file.txt (in the "decrypted" folder)
- Run the script : 
    * Encryption : ```python enc-dec.py -e file.jpg```
    * Decryption : ```python enc-dec.py -d enc-file.jpg```

### Sample results :
- Try opening the encrypted file enc-image.jpg from the encrypted folder.
- Now try opening the decrypted file dec-image.jpg from the decrypted folder.
- Both these files were originally generated from image.jpg. Compare the decrypted file and original file to see if they're the same.

![Sample Results](https://i.imgur.com/SgERi2K.png)