Hunt Username
=============

|checkout| |withlove| |opensource| |BashShell| |Linux|

Hunt Username is a simple Bash Script that searches for a username on
various social channels(Github, Dev.To, Reddit) and then displays
whether an account exists with that username.This script can be used for
searching for a person on various social channels.

Dependencies
------------

-  cURL

Setup Instructions
------------------

-  Installing cURL:

   .. code-block:: bash

      sudo apt install curl

-  For running the script when we are in the same directory where
   **huntUsername.sh** resides, execute the following command.

   .. code-block:: bash

      bash huntUsername.sh

-  For the running script from anywhere regardless of the directory the
   current user is in, move the file **huntUsername.sh** to
   **/usr/local/bin**.

   1. To do so execute the following command:

      .. code-block:: bash

         sudo cp huntUsername.sh /usr/local/bin

   2. Then give execute permission to the script. For adding execute permission, run the following command:

      .. code-block:: bash

         sudo chmod +x /usr/local/bin/huntUsername.sh

   3. Now you can run the script using the follwing command:

      .. code-block:: bash

         huntUsername.sh

Usage
-----

Using the script is fairly simple, just type the following command if you want to provide the username when prompted:

.. code-block:: bash

   bash huntUsername.sh

To provide the username as an argument to the script, run the following command:

.. code-block:: bash

   bash huntUsername.sh username

Output
------

.. image:: https://imgur.com/PurqZtD.png
   :alt: sample-output
   :target: https://imgur.com/PurqZtD.png

Author(s)
---------

Made By `Ashutosh Kumar <https://github.com/Blastoise>`_

.. |checkout| image:: https://forthebadge.com/images/badges/check-it-out.svg
   :target: https://github.com/HarshCasper/Rotten-Scripts/tree/master/Bash/Hunt_Username/
.. |withlove| image:: https://forthebadge.com/images/badges/built-with-love.svg
   :target: https://forthebadge.com
.. |opensource| image:: https://forthebadge.com/images/badges/open-source.svg
   :target: https://forthebadge.com
.. |BashShell| image:: https://img.shields.io/static/v1?label=MADE%20WITH&message=BASH&color=red&style=for-the-badge&logo=gnu-bash
   :target: https://shields.io/
.. |Linux| image:: https://img.shields.io/static/v1?label=MADE%20FOR&message=LINUX&color=red&style=for-the-badge&logo=linux
   :target: https://shields.io/
