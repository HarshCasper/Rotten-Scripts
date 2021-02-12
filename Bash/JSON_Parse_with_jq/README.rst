JSON parsing in bash
====================

|checkout|

``find_flag.sh`` script will tell you how to use `jq <https://stedolan.github.io/jq/>`__ command to parse JSON file in bash with an example (``sample.json``)

The script will run below 3 commands and find the flag from the
``sample.json`` file

.. code:: bash

   $ cat sample.json | jq "." | head -n 13

.. code:: bash

   $ cat sample.json | jq ".data.allPosts.edges[0:3]"

.. code:: bash

   $ cat sample.json | jq ".data.allPosts.edges" | grep -E -o 'RotteN{.*}' | grep -v 'harder'

.. |checkout| image:: https://forthebadge.com/images/badges/check-it-out.svg
   :target: https://github.com/HarshCasper/Rotten-Scripts/tree/master/Bash/JSON_Parse_with_jq/
