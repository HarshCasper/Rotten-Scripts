Video Steganography
===================

|checkout|

Steganography is the practice of concealing a file, message, image, or
video within another file, message, image, or video. It has existed for
a long time, and nowadays, digital steganography is used to hide data
inside images. We can hide all kinds of data by using different digital
stenographic methods.

Steganography
-------------

A digital image is a representation of pixel values, and every pixel
value will have numbers containing information regarding the pixel. A
digital color image will have **red, green, and blue channels** and
eight bits to represent each channel, so every channel can take a value
from **0-255**, and this value represents the intensity of the pixel.

.. code-block:: python

   (R, G, B)=(0,0,0)

This is the representation of the color black and this represents the
color white.

.. code-block:: python

   (R, G, B)=(255,255,255) 

Take an array of pixels as an example and suppose we want to hide the
character A in it. This is how we will do it:

.. code-block:: python

   (R, G, B)= (11101010 11101001 11001010),(10111001,11001011,11101000),(11001001 00100100 11101001)

This is a pixel array, and we want to hide A in it. The ASCII value of A
is 65. If we convert it to binary, we get 01000001. So if we use LSB
transformation, we can change the LSB of all the numbers in our array
and get:

.. code-block:: python

   (R,G, B)= (11101010 11101001 11001010),(10111000,11001010,11101000),(11001000 00100101 11101001)

Image Steganography
-------------------

Image steganography can be simply done using the ``stegano`` package in
python. - First we will import lsb

.. code-block:: python

   from stegano import lsb

-  To hide a text in an image named file.png

.. code-block:: python

   secret =  lsb.hide("file.png", "text")

-  To save the encoded image in a file named e_file.png

.. code-block:: python

   secret.save("e_file.png")

-  To decode the secret from the file e_file.png

.. code-block:: python

   lsb.reveal("e_file.png")

.. _video-steganography-1:

Video Steganography
-------------------

As we know video is a collection of frames, where each frame is a
picture. So what in this script frames were extracted from the video and
the hidden message is embedded in these frames and then they are
stitched together and saved into another file named
“Embedded_Video.mp4”. So to decode the hidden message use the
“Embedded_Video.mp4” file.

Packages Used
-------------

-  stegano
-  cv2
-  numpy
-  time
-  math
-  os
-  shutil
-  ffmpeg
-  subprocess

.. |checkout| image:: https://forthebadge.com/images/badges/check-it-out.svg
  :target: https://github.com/HarshCasper/Rotten-Scripts/tree/master/Python/Video_Steganography/

