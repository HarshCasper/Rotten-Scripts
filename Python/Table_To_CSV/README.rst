Table to CSV/EXCEL
==================

|checkout| |forthebadge made-with-python| |Built Jupyter|

*This README explains various things that one must know before using the
script.* **KINDLY** *go through the whole file.*

This **template** script converts an image of table ``.png`` file into
``.csv`` or ``.xlsx``.

All the steps are properly mentioned as comments in the script.

Short description of package/script
-----------------------------------

-  Takes ``.png`` or ``.jpg`` of a table (prefer .png) as input.
-  Scans the image.
-  Determine the structure and boundaries of the table.
-  Reads the cell content.
-  Converts the file in ``.csv`` or ``.xlsx``.

Dependency
----------

This script has multiple dependencies, see `requirements.txt <requirements.txt>`__. Most Notable ones are-

1. `Numpy <https://numpy.org/>`__
2. `Pandas <https://pandas.pydata.org/>`__
3. `OpenCV <https://opencv.org/>`__
4. `Tesseract <https://github.com/tesseract-ocr/tesseract>`__
5. `Matplotlib <https://matplotlib.org/>`__
6. `Jupyter <https://jupyter.org/>`__ ## Setup instructions

-  Set up a `Virtual Environment <https://www.geeksforgeeks.org/python-virtual-environment/#:~:text=A%20virtual%20environment%20is%20a,of%20the%20Python%20developers%20use.>`__.

-  Run the command ``pip3 install -r requiremnts.txt``

-  Make sure you have Tesseract.exe installed. `See this <https://github.com/tesseract-ocr/tesseract/wiki>`__ and `this <https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i>`__

.. important::

   These are the only steps required to setup the script. But this script
   basically is a template which can be used as a starting point by others.
   (More Details in the Next Section)

-  In the script, feed the path to the image file, and carefully change the destination path.
-  Make sure you follow the guidelines.
-  Carefully choose whether to convert in ``.csv`` (by pressing ‘c’) or ``.xlsx`` (by pressing ‘x’).
-  Conversion Complete.

Detailed explanation of template
--------------------------------

The Script is basically a *template* that can be further edited
according to the needs. This issue arises due to the fact that there is
no set table structure. For every table structure there needs to certain
changes in the code which can be easily achieve using the interactive
`Jupyter Notebook <table_convert.ipynb>`__. Follow the comments in the
Notebook to make the changes. It is much more interactive than the
``.py`` file.

Also Encoding is a major issue in case of Excel File as different
version of Excel uses different encoding techniques. Most Popular being
``utf-8`` and ``Windows-1252`` or ``CP-1252``.

Although I have used ``XlsxWriter`` as engine, there are various other
engine which can be used according to different needs.

Output
------

Test Image

.. figure:: img/test.PNG
   :alt: Test

Grid Marked

.. figure:: img/grid.PNG
   :alt: Grid

Terminal Options

.. figure:: img/option.PNG
   :alt: option

Resulted CSV

.. figure:: img/csv_img.PNG
   :alt: CSV

Resulted Excel

.. figure:: img/excel_img.PNG
   :alt: Excel

Author(s)
---------

Made by `Vybhav Chaturvedi <https://www.linkedin.com/in/vybhav-chaturvedi-0ba82614a/>`__

.. note::

   It is not possible to convert every table into a ``.csv`` or ``.xlsx``
   without using Sequential Deep Learning, which is not the aim of this
   project. I have basically provided a small template which can be used to
   convert every possible table, but is not universal at all.

In case you find trouble with the conversion. **Don’t
bombard**\ `Rotten-Scripts <https://github.com/HarshCasper/Rotten-Scripts>`__\ **with
issues and PRs** follow this `link <https://github.com/vybhav72954/My_Junk>`__ here you can open
issues and launch PRs.

.. |forthebadge made-with-python| image:: http://ForTheBadge.com/images/badges/made-with-python.svg
   :target: https://www.python.org/
.. |Built Jupyter| image:: https://img.shields.io/badge/Built%20Using-Jupyter-orange?style=for-the-badge&logo=Jupyter
   :target: table_convert.ipynb
.. |checkout| image:: https://forthebadge.com/images/badges/check-it-out.svg
  :target: https://github.com/HarshCasper/Rotten-Scripts/tree/master/Python/Table_To_CSV/

