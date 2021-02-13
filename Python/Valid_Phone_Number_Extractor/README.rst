Valid Phone Number extractor
============================

|checkout|

A simple Python Script to spit out all the mobile numbers or phone
numbers or both (according to user’s requirements) to the output text
file while taking text from the input text file.

Usage
-----

-  Keep input file in the same folder/directory as of the script. Or,
   enter path to input file relative to the location of the script.
-  Run the following command ``python3 num_from_text.py -h`` for any
   help.

You should receive following output which pretty much explains all the
flags/arguments you can pass in through command line interface (CLI)

.. code-block:: bash

   usage: num_from_text.py [-h] [--mobile MOBILE] [--phone PHONE] [--all ALL]
                           [--output OUTPUT]

   Find mobile or phone numbers from input text file.

   optional arguments:
     -h, --help            show this help message and exit
     --mobile MOBILE, -m MOBILE
                           Extract mobile numbers only.
     --phone PHONE, -p PHONE
                           Extract Phone Numbers only.
     --all ALL, -a ALL     Extract both Mobile Numbers and Phone Numbers.
     --output OUTPUT, -o OUTPUT
                           Name of output file.

.. note::
   
   If ``--output`` is not specified default file names will be used as output file name.

.. |checkout| image:: https://forthebadge.com/images/badges/check-it-out.svg
  :target: https://github.com/HarshCasper/Rotten-Scripts/tree/master/Python/Valid_Phone_Number_Extractor/

