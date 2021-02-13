Scrap Resturants using the Zomato API
=====================================

|checkout|

Description
-----------

This Python Script Scraps Resturants using API Key of Zomato

Get a Zomato API Key
--------------------

-  Log in or create a free account on `Zomato <https://www.zomato.com/>`__
-  Navigate to their `developers page <https://developers.zomato.com/api>`__, click on the “Generate
   API Key” button.

   -  The API requires that you enter your phone number, Company
      Website/Blog

Execution
---------

-  Run ``pip install - r requirements.txt``
-  Create a ``.env`` file like as ``.env.example``, and add follwoing
   line with your API Key which you get from above Steps.

::

   projectKey = {put your key here without brackets}

   cityName = {add City Name Here}

-  Run ``python main.py``

Run Programs In Order: |Terminal|

You Will Get Output Like This:

.. figure:: https://i.pinimg.com/originals/ef/6d/c1/ef6dc17845920a580eaffd21e09433fb.png?epik=dj0yJnU9b1EyenIyQnpfUzJLa2w4MllTR2dFQjBDMkh3RU1NdWImcD0wJm49ZWFfeHRxUGphTWdWMWZwU0VnQ09XUSZ0PUFBQUFBR0FWQVZB
   :alt: Output

.. |Terminal| image:: https://i.pinimg.com/originals/98/11/39/981139102df3bfa5b776a626bec42501.png?epik=dj0yJnU9S0stamItZ0kwY3hnN3RUTGI1dC1qSEtnTDh4OXpsWDAmcD0wJm49RmtIQUVpYzl2eUNYRGtpb3RVbHRBdyZ0PUFBQUFBR0FWQVc0

.. |checkout| image:: https://forthebadge.com/images/badges/check-it-out.svg
  :target: https://github.com/HarshCasper/Rotten-Scripts/tree/master/Python/Scrap_Restaurants_using_ZomatoAPI/

