
# Delete Tweets Automatically

This is a utility to delete your tweets using python program

## Requirements

**credentials.json**: This file contains the credentials for accessing the twitter API. Generate the same from your twitter developer account and paste in this file

***Format of 'credentials.json' file***

    {
        "consumer_key": "",
        "consumer_key_secret": "",
        "bearer_token": "",
        "access_token": "",
        "access_token_secret": ""
    }

### Usage

After cloning the project in your local directory, download the required packages using the command:

    pip3 install -r requirements.txt

After all the required packages are installed, run the program using the following command.

    python3 main.py --path P --param M [--count C] [--min N] [--max N] [--hours H] [--days D] [--verbose]

### Arguments

    --path P : Path to the 'credentials.json' file on your local system. It is a mandatory argument.

    --param M : Method of filtering the tweets. Pass one of the following: ['retweet', 'likes', 'time']. It is also a mandatory argument.

    --count C : Number of tweets to be considered while filtering. It is set to 20 by default.

    --min N : Minimum threshold of the parameter (retweet/likes). Set to 0 by default.

    --max N : Maximum threshold of the parameter (retweet/likes). Set to the maximum value of INT by default.

    --hours H : No of hours to go back from the current time for filtering tweets. Set to 0 by default.

    --days D : No of days to go back from current time for filtering tweets. Set to 0 by default.

    --verbose : Prints the tweets before deleting them.

You can also run the following command for any help about any argument.

    python3 main.py -h
