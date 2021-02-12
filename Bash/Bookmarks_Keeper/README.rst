Bookmarks Keeper
================

|checkout| |built_love| |open_source| |with_markdown| |BashShell|

Bookmarks Keeper is a simple bash script which when executed with out
any argument gets all the bookmarks from all the major browsers(Google
Chrome, Mozilla Firefox, Brave Browser and Chromium) installed on your
system and stores all the bookmarks in a markdown file named
bookmarks.md. This script when used with a task scheduler can be used
for bookmark backup. This script can also take a single argument and
search for bookmarks with that particular pattern and stores them in
bookmarks.md file.

Setup Instructions
------------------

-  For running the script when we are in the same directory where
   bookmarksKeeper.sh resides, execute the following command.

   .. code-block:: shell

      bash bookmarksKeeper.sh

-  For the running script from anywhere regardless of the directory the
   current user is in, move the file **bookmarksKeeper.sh** to
   **/usr/local/bin**.

   1. To do so execute the following command:

      .. code-block:: bash

         sudo cp bookmarksKeeper.sh /usr/local/bin

   2. Then give execute permission to the script.For adding execute permission, run the following command:

      .. code-block:: bash

         sudo chmod +x /usr/local/bin/bookmarksKeeper.sh

   3. Now you can run the script using the follwing command:

      .. code-block:: bash

         bookmarksKeeper.sh

Usage
-----

To get all the bookmarks regardless of filtering, run the script as
follows(assuming script is not located in /usr/local/bin and we are in
the same directory where bookmarksKeeper.sh is located):

.. code-block:: bash

   bash bookmarksKeeper.sh

We can also provide an argument to the script to filter out and store
only those bookmarks in the markdown file which contains that argument.

To doing so execute the following command:

.. code-block:: bash

   bash bookmarksKeeper.sh mozilla

.. note::

   To change the location where the markdown file will be stored, you can
   modify the **location** variable in the script.

Output
------

.. image:: https://imgur.com/zV7HCU8.png
   :alt: sample-output
   :target: https://imgur.com/zV7HCU8.png

Author(s)
---------

Made By `Ashutosh Kumar <https://github.com/Blastoise>`_

.. |checkout| image:: https://forthebadge.com/images/badges/check-it-out.svg
   :target: https://github.com/HarshCasper/Rotten-Scripts/tree/master/Bash/Bookmarks_Keeper/
.. |built_love| image:: https://forthebadge.com/images/badges/built-with-love.svg
   :target: https://forthebadge.com
.. |open_source| image:: https://forthebadge.com/images/badges/open-source.svg
   :target: https://forthebadge.com
.. |with_markdown| image:: https://forthebadge.com/images/badges/made-with-markdown.svg
   :target: https://forthebadge.com
.. |BashShell| image:: https://badges.frapsoft.com/bash/v1/bash.png?v=103
   :target: https://github.com/ellerbrock/open-source-badges/
