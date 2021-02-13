Image Steganography
===================

|checkout|

Given a string and an image, the python scripts hides the string in the
image based on Least Significant Bit technique. In the technique the
given string is converted to its ASCII integer values and then further
converted into binary. Then based on the digits in the binary
representation, the brightness value of the least significant pixel is
changed. This small change can not be distinguished by the naked eye.

Setting up:
-----------

-  Create a virtual environment and activate it
-  Install the requirements

.. code:: sh

     $ pip install pillow

Running the script:
-------------------

.. code:: sh

     $ # To encode text in the image
     $ python steganography.py encode [image_path]  
     $ # the scripts then asks for the secret message
     $ #
     $ # To decrypt the secret_text
     $ python steganography.py decode [path_of_encrypted_image]

Example running the script
--------------------------

.. code:: sh

     $ python steganography.py encode input.jpg
 
.. |checkout| image:: https://forthebadge.com/images/badges/check-it-out.svg
  :target: https://github.com/HarshCasper/Rotten-Scripts/tree/master/Python/Image_Steganography/

