# Image Steganography

Given a string and an image, the python scripts hides the string in the image based on Least Significant Bit technique.<br>
In the technique the given string is converted to its ASCII integer values and then further converted into binary. Then based on the digits in the binary representation, the brightness value of the least significant pixel is changed. This small change can not be distinguished by the naked eye.

## Setting up:

- Create a virtual environment and activate it

- Install the requirements

```sh
  $ pip install pillow
```

## Running the script:

```sh
  $ # To encode text in the image
  $ python steganography.py encode [image_path]  
  $ # the scripts then asks for the secret message
  $ #
  $ # To decrypt the secret_text
  $ python steganography.py decode [path_of_encrypted_image]
```

## Example running the script

```sh
  $ python steganography.py encode input.jpg  
```
