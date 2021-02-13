Python News Reader
===================

|checkout| |forthebadge made-with-python|

This **Python** program fetches the news from Indian sources and speaks
or reads the news with voice over feature. A python script which will
fetch news from **newsapi.org** and will speak that news with headlines
and description. Reading news and articles sometimes may too time
consuming and boring ,With the help of this python program you can
listen to top news while working on your other work.

What is News API?
-----------------

News API is a simple HTTP REST API for searching and retrieving live
articles from all over the web. Visit the newsapi.org for documentation
and your personal API key.

Steps to run this script on your local machine:
-----------------------------------------------

1. Firstly, download the file
“Rotten-Scripts/Python/Python_news_reader” on your machine.

2. In the same downloaded directory, open the Window PowerShell
and run the following command to install the dependencies:

.. code-block:: bash

   pip install -r requirements.txt

3. Make a file of **.env** extension and make a **API_Key=**
variable in that file (Take reference from **.env.example** file.) and
save that file.

4. Visit newsapi.org and copy your API key from there. Now assign
your API Key to environment variable that you made previously in
**.env** file and save the file. i.e

.. code-block:: bash

   API_Key=YOUR_API_URL_HERE

5. Make sure you have a proper internet connection. Now, you are
all set to use this script. Open the “Python news reader.py” file to run
the script.

*Now, Enjoy listening to top news from all over the world. 👍*

.. |forthebadge made-with-python| image:: http://ForTheBadge.com/images/badges/made-with-python.svg
   :target: https://www.python.org/
.. |checkout| image:: https://forthebadge.com/images/badges/check-it-out.svg
  :target: https://github.com/HarshCasper/Rotten-Scripts/tree/master/Python/Python_news_reader/

