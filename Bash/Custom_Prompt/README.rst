Custom Command Prompt on Bash
=============================

|checkout| |BashShell| |Linux|

By default Bash command prompts are boring and show no extra
information. You can tweak your command prompt to show a variety of
information such as ``git`` and virtual environment, command execution
time, previous command status, current directory, SSH session and many
more can be added.

Prerequisite
------------

You must have ``git`` installed in order to use this script. If you
haven’t already follow the step below

.. code:: bash

   sudo apt-get update && sudo apt-get install -y git

Setup Instructions
------------------

-  Open your ``.bashrc`` in ``nano`` or ``vim`` or any editor of your
   choice.

   .. code:: bash

      sudo nano ~/.bashrc

-  Goto the last of your ``.bashrc`` and paste everything from the file
   `custom_prompt.sh <custom_prompt.sh>`__. *Do not change anything else
   until you know. You can however customise the colors of your choice*

-  Save your ``.bashrc`` and exit

   .. code:: bash

      # for nano
      CTRL + O
      CTRL +X

      # for vim
      :w
      :q

-  Run the following command to load new configuration.

   .. code:: bash

      source ~/.bashrc

Author(s)
---------

Made by `Avinal Kumar <https://github.com/avinal>`__

.. |checkout| image:: https://forthebadge.com/images/badges/check-it-out.svg
   :target: https://github.com/HarshCasper/Rotten-Scripts/tree/master/Bash/Custom_Prompt/
.. |BashShell| image:: https://img.shields.io/static/v1?label=MADE%20WITH&message=BASH&color=red&style=for-the-badge&logo=gnu-bash
   :target: https://shields.io/
.. |Linux| image:: https://img.shields.io/static/v1?label=MADE%20FOR&message=LINUX&color=red&style=for-the-badge&logo=linux
   :target: https://shields.io/
