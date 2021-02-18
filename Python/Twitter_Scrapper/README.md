## Twitter Scrapper

This script extracts all Tweets, Retweets, Images, Videos, Hashtags, Likes and Pinned tweet of a specific user in a .csv file.

![How to use the script](https://i.ibb.co/mcjK65f/Tweeter-Scrapper.png)

### Requirements

1. The system should have  **python**  and  **tweepy**  installed. Also, the user should have a  **Twitter developer account**  and a  **Twitter app**  (if you do not have one, create one at  [here](https://developer.twitter.com/)). The use of Tweepy and need for a developer account is in accordance with the Twitter scraping rules.
2.  Chrome Driver (that matches your chrome version.) -- platform dependent.

### Setup

1.  Create a Virtual Environment.
2.  Install the requirements by using  `pip install -r requirements.txt`
3. Open the script in any text editor/IDE
4. Get the credentials from the app created by you on twitter developer account and enter them here.
5. Also add the path to your chrome driver in the PATH_CHROME_DRIVER constant
6.  Hurray.! You're ready to use the script to extracts all Tweets, Retweets, Images, Videos, Hashtags and Likes of a specific user.

### Running a File

1.  Run the Script  `python twitter_scrapper.py`
3.  Enter the username you want the information from.
4. Finally, you need to enter a Twitter username and password in order to extract the pinned Tweet (if it exists)
5. The .csv file is downloaded to the folder where the file runs.