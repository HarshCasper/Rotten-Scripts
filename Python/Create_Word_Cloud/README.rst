Create a Word Cloud
===================

|checkout|

Takes a text file, preprocesses the content by removing stopwords,
creates a wordcloud out of them and saves this wordcloud as a PNG.

Steps
-----

-  Installation

   1. Using pip

   .. code-block:: bash

      pip install wordcloud

   2. Download the .whl compatible with your Python version and your Windows distribution (32bit or 64bit) from `here <https://www.lfd.uci.edu/~gohlke/pythonlibs/#wordcloud>`__ cd to the file path

   .. code-block:: bash

      python -m pip install <filename>

.. note::

   If pip doesn’t install the wheel, it’s probably because you’re
   using 32bit Python. I would suggest using 64bit python for which
   there is a wheel.

-  Using the script

   1. To get a basic wordcloud

   .. code-block:: bash

      python create_word_cloud.py --text <filename>

   2. To get a wordcloud with a specific background

   .. code-block:: bash

      python create_word_cloud.py --text <filename> --background <color>

   3. To get a wordcloud in the shape of a mask

   .. code-block:: bash

      python create_word_cloud.py --text <filename> --mask <filename>

   .. note::

      Keep in mind that the background of the mask used must be
      white, otherwise, the system will consider the background as an
      object. In addition, the background cannot be transparent,
      because transparent colors will be considered black.

   4. To get a border of the mask with the wordcloud

   .. code-block:: bash

      python create_word_cloud.py --text <filename> --contour_width <integer>

   .. note::

      This will need a mask. Also, the default color is black.

   5. To get a colored border of the mask with the wordcloud

   .. code-block:: bash

      python create_word_cloud.py --text <filename> --contour_color <color>

   .. note::

      This will need a mask and a contour width.

   6. To get a wordcloud in the colors based on the mask

   .. code-block:: bash

      python create_word_cloud.py --text <filename> --color_func 1

      You can also use all of the flags together, like this:

   .. code-block:: bash

      python create_word_cloud.py --text <filename> --background <color> --mask <filename> --contour_width <integer> --contour_color <color> --color_func 1

.. |checkout| image:: https://forthebadge.com/images/badges/check-it-out.svg
  :target: https://github.com/HarshCasper/Rotten-Scripts/tree/master/Python/Create_Word_Cloud/

