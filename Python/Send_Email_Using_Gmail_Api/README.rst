Getting Started With Google Api
===============================

|checkout|

1. If you don’t already have a Google account, `sign up <https://www.google.com/accounts>`__.
2. If you have never created a Google APIs Console project, read the `Managing Projects page <http://developers.google.com/console/help/managing-projects>`__ and create a project in the `Google API Console <https://console.developers.google.com/>`__.

Gmail Api
---------

The Gmail API is a RESTful API that can be used to access Gmail
mailboxes and send mail. All we need to use the Gmail API is the `client library <https://developers.google.com/gmail/api/downloads#python>`__ and an app that can `authenticate <https://developers.google.com/gmail/api/auth/about-auth>`__
as a Gmail user.

Setup
-----

Above script uses OAuth 2.0 authentication.

`Generate a client ID and client secret <https://developers.google.com/gmail/api/quickstart/python>`__
Follow steps until you generate ``credentials.json``. Save this file in your project folder.

Run Script On Windows
---------------------

1. run ``py -m venv env``
2. run ``.\env\Scripts\activate``
3. run ``pip intall -r requirements.txt``
4. run ``python auth.py"``
5. run ``python script.py "reciver_email_address" "subject_of_mail" "message_of_mail"``

Run Script On macOS and Linux
-----------------------------

1. run ``python3 -m venv venv``
2. run ``source venv/bin/activate``
3. run ``pip3 intall -r requirements.txt``
4. run ``python auth.py"``
5. run ``python script.py "reciver_email_address" "subject_of_mail" "message_of_mail"``

.. |checkout| image:: https://forthebadge.com/images/badges/check-it-out.svg
  :target: https://github.com/HarshCasper/Rotten-Scripts/tree/master/Python/Send_Email_Using_Gmail_Api/

