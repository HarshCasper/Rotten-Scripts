RSA Key Pair Generator
======================

|checkout|

About RSA Encryption Algorithm
------------------------------

RSA algorithm is asymmetric cryptography algorithm. Asymmetric actually
means that it works on two different keys i.e. Public Key and Private
Key. As the name describes that the Public Key is given to everyone and
Private key is kept private.

An example of asymmetric cryptography :

-  A client (for example browser) sends its public key to the server and requests for some data.
-  The server encrypts the data using client’s public key and sends the encrypted data.
-  Client receives this data and decrypts it.
-  Since this is asymmetric, nobody else except browser can decrypt the data even if a third party has public key of browser

**The Public key is used to encrypt the data and Private key is used for decrypting the data**

Explanation of code
-------------------

-  We have used forge package of node to create RSA keys
-  First we import the package node-forge and use Public Key Infrastructure(pki) module of forge package to generate RSA keys
-  rsa.generateKeyPair creates a new key pair with random modulus. The first parameter specifies the modulus/key size in bits, second the exponent

To run the code
---------------

1. Clone the folder
2. Inside the project directory open command line
3. npm Install
4. node rsaKeyPairGenerator.js

Output
------

The output will be in the form of JSON Object named keys, having public
and private keys.

.. image:: rsaKeyPairGenerator.png

Author(s)
---------

Made by `Mohit Bhat <https://github.com/mbcse>`__.

.. |checkout| image:: https://forthebadge.com/images/badges/check-it-out.svg
   :target: https://github.com/HarshCasper/Rotten-Scripts/tree/master/JavaScript/RSA_Key_Pair_Generator/
