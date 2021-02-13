Building a Twitter Bot with Python
==================================

|checkout|

Do you use Twitter? If so, then you must come across some of the bots
that like, retweet, follow, or even reply to your tweets. But have you
ever wondered how they are made? Well, it’s easy as filling water in a
bottle. Haha! It’s really not rocket science. So, let’s get started and
make a bot.

.. figure:: https://media.makeameme.org/created/bots-bots-9c4m68.jpg
   :alt: image

In Python, the twitter bot is just a few lines of code, less than 30.

Prerequisites for making one (Bot)
----------------------------------

::

   1. Twitter developer account.
   2. tweepy module in Python.
   3. A twitter account, which you want to make a bot.

Understanding the code
----------------------

.. figure:: https://dev-to-uploads.s3.amazonaws.com/i/6hwd9o5kt84jyjbiemos.png
   :alt: image

You see there are no more than 30 lines in Python. Let’s understand each
and every line.

.. code-block:: python

   import tweepy
   import time

To communicate with Twitter API, we need some module, here we are using
**tweepy**. You can install it easily.

.. code-block:: python

   pip install tweepy

Once you install the module, write some more code.

.. code-block:: python

   # Authenticate to Twitter
   CONSUMER_KEY = '<your-consumer-or-API-key-goes-here>'
   CONSUMER_SECRET = '<your-consumer-or-API-secret-goes-here>'
   ACCESS_KEY = '<your-access-key-goes-here>'
   ACESS_SECRET = '<your-access-secret-goes-here>'
   auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
   auth.set_access_token(ACCESS_KEY, ACESS_SECRET)

This is used to authenticate your Twitter account. Remember these keys
are of your account, don’t share them to anyone, else they can access
your data. That’s why I have made some variables in which I will store
the keys.

These keys will be found in your developer account, which you’ve saved a
time ago.

**auth** variable is created to authenticate the account, Twitter uses
OAuth to do this.
And, after that, we will set the tokens.

.. code-block:: python

   # Create API object
   api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

This class provides a wrapper for the API as provided by Twitter. If you
stuck somewhere, you can always refer to the `tweepy documentation <http://docs.tweepy.org/en/latest/>`__.

.. code-block:: python

   user = api.me()
   search = '#python3'
   numTweet = 500
   for tweet in tweepy.Cursor(api.search, search).items(numTweet):
       try:
           print('Tweet Liked')
           tweet.favorite()
           print("Retweet done")
           tweet.retweet()
           time.sleep(10)
       except tweepy.TweepError as e:
           print(e.reason)
       except StopIteration:
           break

Finally, we will tell the program to look for the keyword **#python3**
in a tweet and the number of tweets that will be processed once in a
day. If you want to like, you can use **tweepy.favorite()** , and for
retweet **tweepy.retweet()**. The reason, I’m using sleep is, twitter
has some guidelines, you must follow otherwise, your account will be
restricted. There is a limit for liking the number of tweets. If it
gives some error, we can use **tweepy.TweepError** so that we know, what
went wrong.

Here’s my bot.

.. figure:: https://dev-to-uploads.s3.amazonaws.com/i/yv731bysoy4jscv8cz5w.png
   :alt: Alt Text

For full process, refer to my `blog <https://dev.to/seema1711/making-a-twitter-bot-with-python-3ld7>`__.

It’s time to build your own bot. All the best.

.. |checkout| image:: https://forthebadge.com/images/badges/check-it-out.svg
  :target: https://github.com/HarshCasper/Rotten-Scripts/tree/master/Python/Twitter_Bot/

