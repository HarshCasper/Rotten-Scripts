How to Launch Computer Programs Using Python
============================================

|checkout|

A Python script can start other programs on your computer.

For example, it can open up the calculator (to do calculations) or it
can open up notepad (so that you can write a document). Or it can open
up a sound file that can be played.

Python has the low-level functionality to be able to open up any program
on your operating, just as if you had double-clicked on it (to get it
started).

You can do this in Python using the ``subprocess.Popen()`` function.

Using this function, all you have to do is pass in the program that you
want to open up in its parameters.

Some examples below.
--------------------

.. code-block:: python

  import subprocess
  subprocess.Popen('C:\\Windows\\System32\\calc.exe')

The code above will open up notepad on a Windows computer.

.. |checkout| image:: https://forthebadge.com/images/badges/check-it-out.svg
  :target: https://github.com/HarshCasper/Rotten-Scripts/tree/master/Python/launching_programs_from_python/

