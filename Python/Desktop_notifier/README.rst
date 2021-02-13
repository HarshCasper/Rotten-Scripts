Desktop Notifier
================

|checkout|

Description
-----------

A desktop notifier app runs on your system and it will be used to send
you notifications after every specific interval of time. - This notifier
will gives news at a particular time interval.

Language
--------

- Python

Checklist
---------

+-----------------------------------+-----------------------------------+
| Name                              | About                             |
+===================================+===================================+
| Desktop Notifier                  | Shows the news on the desktop at  |
|                                   | the specific interval of time.    |
+-----------------------------------+-----------------------------------+

Installation
------------

.. code:: bash

   $ pip install notify2
   $ pip install feedparser
   $ pip install pygame

Usage
-----

To access the ``notifier``, this application imports the following
modules.

.. code:: python

   import os
   import time
   import feedparser
   import notify2
   from pygame import mixer

Instructions to run this application
------------------------------------

-  Download and Run the **desktop_notifier.py**
-  It will give notifications of news with a particular interval of time
   on your system.

.. note::

   If the script will be showing the dbus error then, create a virtual environment for that.

Steps to create the virtual environment (for windows)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. pip install virtualenv
2. pip install pipenv
3. pipenv –help (for help)
4. pipenv install
5. pipenv shell
6. pip install the packages
7. execute the program

.. |checkout| image:: https://forthebadge.com/images/badges/check-it-out.svg
  :target: https://github.com/HarshCasper/Rotten-Scripts/tree/master/Python/Desktop_notifier/

