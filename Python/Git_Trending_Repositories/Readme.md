### Scrape Git Trending respositories

This script is scrapes details about Git trending repositories displayed here https://github.com/trending.

The data will be exported in a .csv file.

### Setup

1. Create a Virtual Environment.
2. Install the requirements by using `pip3 install -r requiremnts.txt`
3. Hurray.! You're ready to use the script.

### Running a file

`python git-trending-repository-scraper.py`

### Running this script as a cron job

The syntax is:

`mm hh * * * <location where python3 is installed> <location of the python script>`

This will execute the cron job everyday at a particular hour.

`0 12 * * * /usr/bin/python3 /home/user/Rotten-Scripts/Python/Git_Trending_Repositories/git-trending-repository-scraper.py`

Adding the above command in the `crontab` will run the script at 12:00 am every day.

`.csv` file will be generated in the directory where the script file is.

The only downside of the cron job is, to install all the requirements globally.


