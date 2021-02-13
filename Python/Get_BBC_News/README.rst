Get BBC News
============

|checkout|

This Python script allows you to get a list of the top 10 news from the
BBC Website.

It displays the headline, and if interested, you can click on the link
to read the entire article.

Requirements
------------

1. requests
2. python-dotenv

Installation
------------

Run the following command to install the python-dotenv module:

.. code-block:: bash

   pip install python-dotenv

Environment variable
--------------------

**BBC_API** in the environment variable must be set by the user with the
URL of the API to be used.

Steps:
^^^^^^

1. Make a file : **.env**
2. Make a variable BBC_API and assign a value to it :

.. code-block:: bash

   BBC_PATH="YOUR_API_URL_HERE"

Working
-------

Run the following command to see the headlines, with the respective
links, on the command line.

.. code-block:: bash 

   python get_news.py

.. |checkout| image:: https://forthebadge.com/images/badges/check-it-out.svg
  :target: https://github.com/HarshCasper/Rotten-Scripts/tree/master/Python/Get_BBC_News/

