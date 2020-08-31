from Crypto.PublicKey import RSA
key = RSA.generate(2048) 
f = open("private_key.pem", "wb")
f.write(key.exportKey('PEM'))
f.close()

public_key = key.publickey()
f = open("public_key.pem", "wb")
f.write(public_key.exportKey('OpenSSH'))
f.close()
