Github_Traffic
==============

|checkout|

This script, can help one determine all the unique viewers on his/her
Repository. By using ``access-token`` one can determine the viewers and
number of time they viewed the Repo. Currently data of only 14 days is
possible (limitation of GitHib-API), but in future by using the GraphQL
queries, this limitation can be answered. The script uses PickleDB, the
data can be imported in CSV as well, although the functionality hasn’t
been added till this point of time.

.. note::

   This script can be converted in a Bot, Action or GitHub app!!!

Dependency
----------

-  githubpy
-  PickleDB
-  python-decouple

These are summarised in ``requirement.txt``

Setup
-----

-  A virtual environment (recommended)
-  ``pip install -r requirements.txt``
-  Generate your own access token from `here <https://github.com/settings/tokens>`__
-  Paste the token in a ``.env`` file (Take `.env.example <.env.example>`__ as an example)
-  It is recommended to paste this token somewhere, as one can’t review it again.
-  Determine the Repository whose traffic you want to view.
-  Run the Script

Usage
-----

Sample Usage -

``python github_traffic.py collect -u vybhav72954 -r Music-Mood-Analysis``

Output -

``2020-12-20T00:00:00Z {'uniques': 1, 'count': 1} 2020-12-24T00:00:00Z {'uniques': 2, 'count': 17} 2020-12-25T00:00:00Z {'uniques': 1, 'count': 4} 2020-12-27T00:00:00Z {'uniques': 1, 'count': 1} 2020-12-28T00:00:00Z {'uniques': 1, 'count': 23} 2020-12-29T00:00:00Z {'uniques': 1, 'count': 1} 2020-12-30T00:00:00Z {'uniques': 1, 'count': 3} 2020-12-31T00:00:00Z {'uniques': 1, 'count': 7}``
Generalized Usage -

-  collect (Collect Information for first time in Database)

``python3 github_traffic.py collect -u [github-user] -r [github-repo]``

-  view (View Information already stored in Database)

``python3 github_traffic.py view -u [github-user] -r [github-repo]``

``2020-12-20T00:00:00Z {"uniques": 1, "count": 1} 2020-12-24T00:00:00Z {"uniques": 2, "count": 17} 2020-12-25T00:00:00Z {"uniques": 1, "count": 4} 2020-12-27T00:00:00Z {"uniques": 1, "count": 1} 2020-12-28T00:00:00Z {"uniques": 1, "count": 23} 2020-12-29T00:00:00Z {"uniques": 1, "count": 1} 2020-12-30T00:00:00Z {"uniques": 1, "count": 3} 2020-12-31T00:00:00Z {"uniques": 1, "count": 7} 8 elements``

Disclaimer
----------

-  ``githubpy`` is a 8 year old package and is no longer maintained
-  Inspired by `this <https://github.com/seladb/github-traffic-stats/blob/master/README.md>`__

Author(s)
---------

Made by `Vybhav Chaturvedi <https://www.linkedin.com/in/vybhav-chaturvedi-0ba82614a/>`__

.. |checkout| image:: https://forthebadge.com/images/badges/check-it-out.svg
  :target: https://github.com/HarshCasper/Rotten-Scripts/tree/master/Python/Github_Traffic/

