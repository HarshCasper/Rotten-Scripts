## Twitter Scrapper

This script extracts all Tweets, Retweets, Images, Videos, Hashtags, Likes and Pinned tweet of a specific user in a .csv file.

### Requirements

1. The system should have  **python**  and  **tweepy**  installed. Also, the user should have a  **Twitter developer account**  and a  **Twitter app**  (if you do not have one, create one at  [here](https://developer.twitter.com/)). The use of Tweepy and need for a developer account is in accordance with the Twitter scraping rules.
2.  Chrome Driver (that matches your chrome version.) -- platform dependent.

### Setup

1.  Create a Virtual Environment.
2.  Install the requirements by using  `pip3 install -r requirements.txt`
3. Create a `.env` file like as `.env.example` and add the credentials from the app created by you on twitter developer account.
4. Also add chrome driver path in .env file
5.  Hurray.! You're ready to use the script to extracts all Tweets, Retweets, Images, Videos, Hashtags and Likes of a specific user.

### Running a File

1.  Run the Script  `python twitter_scrapper.py`
2.  Enter the username you want the information from.
3. Finally, you need to enter a Twitter username and password in order to extract the pinned Tweet (if it exists)
4. The `.csv` file is downloaded to the folder where the file runs.

![How to use the script](https://i.ibb.co/mcjK65f/Tweeter-Scrapper.png)
