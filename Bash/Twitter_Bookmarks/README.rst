Twitter Bookmarks
=================

|checkout| |withlove| |opensource| |mademarkdown| |BashShell| |Linux|

Twitter Bookmarks is an awesome bash script which when executed
appropriately scrapes the URL of all of the tweets bookmarked by you by
signing in to your Twitter account using the credentials provided by you
while running the script. By default it stores the output in a markdown
file name **twitterBookmarks.md** located at **/home/user/**.This script
when used with a task scheduler can be used for generation of data that
can be used for various purposes.

Dependencies
------------

-  cURL
-  jq
-  Appropriate Chrome Web Driver(Same Version that of your Google Chrome Browser)

Setup Instructions
------------------

-  First download the appropriate Chrome Web Driver using the this `link <https://chromedriver.chromium.org/downloads>`__.

-  Install the other two dependencies using the following commands:

   1. Installing cURL:
   
      .. code-block:: bash

         sudo apt install curl

   2. Installing jq:
   
      .. code-block:: bash

         sudo apt-get install jq

-  For running the script when we are in the same directory where
   **twitterBookmarks.sh** resides, execute the following
   command.(Assuming Chrome Driver is located at **/home/user/**)

   .. code-block:: bash

      bash twitterBookmarks.sh

-  For the running script from anywhere regardless of the directory the
   current user is in, move the file **twitterBookmarks.sh** to
   **/usr/local/bin**.(Assuming Chrome Driver is located at
   **/home/user/**.)

   1. To do so execute the following command:

      .. code-block:: bash

         sudo cp twitterBookmarks.sh /usr/local/bin

   2. Then give execute permission to the script.

      For adding execute permission, run the following command:

      .. code-block:: bash

         sudo chmod +x /usr/local/bin/twitterBookmarks.sh

   3. Now you can run the script using the follwing command:

      .. code-block:: bash

         twitterBookmarks.sh

-  Please read the `NOTE <#note>`__ section to know how to specify the location of Chrome Web Driver and for editing other settings.

Usage
-----

Using the script is fairly simple, just type the following command if
you want to provide your username and password when prompted(this does
not show your password while typing):

.. code-block:: bash

   bash twitterBookmarks.sh

To provide the username and password as an argument to the script, run
the following command:

.. code-block:: bash

   bash twitterBookmarks.sh username password

.. note::

   There are few variables that can be modified according to your need.

   1. The most important variable that can be modified is the
      **driver_location** variable that stores the full path of the
      directory where the Chrome Web Driver is situated. By default it will
      search for the Web Driver at **/home/user/**

   2. Another important variable is **sleep_time** which is set to 5 by
      default and describes the number of seconds to wait for the page to
      be loaded. If your internet speed is slow then increase the number
      accordingly.

   3. Last variable that can be tuned is **location_of_file** which stores
      the full path of the file where the output will be stored.

Output
------

.. image:: https://imgur.com/GgVDc2s.png
   :alt: sample-output
   :target: https://imgur.com/GgVDc2s.png

Author(s)
---------

Made By `Ashutosh Kumar <https://github.com/Blastoise>`_

.. |withlove| image:: https://forthebadge.com/images/badges/built-with-love.svg
   :target: https://forthebadge.com
.. |opensource| image:: https://forthebadge.com/images/badges/open-source.svg
   :target: https://forthebadge.com
.. |mademarkdown| image:: https://forthebadge.com/images/badges/made-with-markdown.svg
   :target: https://forthebadge.com
.. |BashShell| image:: https://img.shields.io/static/v1?label=MADE%20WITH&message=BASH&color=red&style=for-the-badge&logo=gnu-bash
   :target: https://shields.io/
.. |Linux| image:: https://img.shields.io/static/v1?label=MADE%20FOR&message=LINUX&color=red&style=for-the-badge&logo=linux
   :target: https://shields.io/
.. |checkout| image:: https://forthebadge.com/images/badges/check-it-out.svg
   :target: https://github.com/HarshCasper/Rotten-Scripts/tree/master/Bash/Twitter_Bookmarks/
