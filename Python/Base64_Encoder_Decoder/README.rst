BASE 64 Encoder Decoder
=======================

|checkout|

About Script
------------

This script is capable of converting some special/secret text into 64
BASE Encoded String

String to Encode and Decode
---------------------------

help
----

.. code-block:: bash

   $ python ConvertToBase64.py --help
   Usage:ConvertToBase64.py [-h] string

   String Encode and Decode

   positional arguments:
     string      Enter String to encode

   optional arguments:
     -h, --help  show this help message and exit

To run
------

.. code-block:: bash

   $ python ConvertToBase64.py (Enter String)

Sample Test
-----------

.. code-block:: bash

   $ python ConvertToBase64.py RottenScripts
   Encoded String:
   b'Um90dGVuU2NyaXB0cw=='
   Want to decode(Y/N):
   Y
   Decoded String:
   RottenScripts

.. |checkout| image:: https://forthebadge.com/images/badges/check-it-out.svg
  :target: https://github.com/HarshCasper/Rotten-Scripts/tree/master/Python/Base64_Encoder_Decoder/

