Custom PowerShell Command Prompt
================================

|checkout|

You can customise your PowerShell prompt to show more informations like
git branch status, command execution time, current directory, admin
status etc. *(This script is just an introduction how you can customise
your PowerShell prompt, you can add several more customizations).* To
read more about PowerShell Prompt go
`here <https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_prompts?view=powershell-7.1>`__.

Dependencies
------------

Git must be installed in order to utilise full potential of the script.
Or you can safely comment the git code in the script. To install Git on
Windows go `here <https://git-scm.com/download/win>`__.

Setup Instructions
------------------

1. Open a PowerShell prompt with admin. You can use ``WinKey + X`` to launch quick tools menu and select **Windows PowerShell (Admin)**
2. Set script execution policy

.. code-block:: powershell

   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force

3. Check if there is an existing configuration, if not create a new file.

.. code-block:: powershell

   if (!(Test-Path -Path $PROFILE)){ New-Item -Path $PROFILE -ItemType File } ; notepad $PROFILE

4. A file will open, if there is an exisiting ``prompt`` function in the file then change the contents else paste everything from `profile.ps1 <profile.ps1>`__ in the file.
5. Save and exit Notepad and relaunch PowerShell.

Output
------

-  Simple mode

.. image:: https://i.imgur.com/W9kOmLA.png
   :alt: simple mode
   :target: https://i.imgur.com/W9kOmLA.png

-  Admin Mode

.. image:: https://i.imgur.com/XBMLkJM.png
   :alt: admin mode
   :target: https://i.imgur.com/XBMLkJM.png

Author(s)
---------

Created by `Avinal Kumar <https://github.com/avinal>`__

.. |checkout| image:: https://forthebadge.com/images/badges/check-it-out.svg
  :target: https://github.com/HarshCasper/Rotten-Scripts/tree/master/PowerShell/Custom_Prompt/
