Text_Extract
============

|checkout| |forthebadge made-with-python|

Text extraction form Images, OCR, Tesseract, Basic Image manipulation
are all important yet very basic scripts.

This script uses ``pytesseract`` for text extraction from images,
considering it only recognizes text and can only print it, this script
additionally adds a functionality to write the text in a ``txt`` and/or
``csv`` file.

Setup instructions
------------------

-  Setup a ``python 3.x`` virtual environment.
-  ``Activate`` the environment
-  Install the dependencies using ``pip3 install -r requirements.txt``
-  You are all set and the `script <text_extract.py>`__ is Ready to run.
-  Carefully follow the Instructions.

Further Readings
----------------

Some newcomers for the first time struggle with Tesseract, this is a
direct link to the `installer <https://github.com/UB-Mannheim/tesseract/wiki>`__

Setting up OCR can be found `here <http://bit.ly/2MClAwD>`__

**PATH** env variable can help in optimizing the code.
`This <http://bit.ly/35d3c3Q>`__ and `this <http://bit.ly/3ba0zmZ>`__
link will help you in order to achieve that.

Usage
-----

Just make sure that Tesseract is in proper directory, run the code
according the comments and guidelines.

::

   Smaple - 
   Enter the Folder name containing Images: <Name of Folder>
   Enter your desired output location: <Name of Folder>

Output
------

Output

.. figure:: img/Output.PNG
   :alt: Output

Image containing Text

.. figure:: img/Sample.PNG
   :alt: Before Compression

After Extraction

.. figure:: img/TextFile.PNG
   :alt: After Backup

Author(s)
---------

Made by `Vybhav Chaturvedi <https://www.linkedin.com/in/vybhav-chaturvedi-0ba82614a/>`__

.. |forthebadge made-with-python| image:: http://ForTheBadge.com/images/badges/made-with-python.svg
   :target: https://www.python.org/
.. |checkout| image:: https://forthebadge.com/images/badges/check-it-out.svg
  :target: https://github.com/HarshCasper/Rotten-Scripts/tree/master/Python/Text_Extract/

