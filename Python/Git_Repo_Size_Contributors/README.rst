Git Repository Size and Contributors List
=========================================

|checkout|

This script will return a CSV file containing Size of the repository and
details of the contributors of the repo. Only the top 500 contributors
are returned by the GitHub API. Read more about this limiting nature
`here <https://docs.github.com/en/rest/reference/repos#list-repository-contributors>`__

How to use?
-----------

``python app.py username_of_repo name_of_repo personal_access_token``

Before running the script, make sure you have the required dependencies.
Not sure about them? Run the following command before running the actual
script:

``pip install -r reqirements.txt``

Working Demo
------------

.. figure:: preview.png
   :alt: image

.. |checkout| image:: https://forthebadge.com/images/badges/check-it-out.svg
  :target: https://github.com/HarshCasper/Rotten-Scripts/tree/master/Python/Git_Repo_Size_Contributors/

