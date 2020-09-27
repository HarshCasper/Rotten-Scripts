# Reddit Data Scrapper
This script will fetch the details of the Subreddit using Reddit API. You can define number of post you want to grab from subreddit, the type of post you want: New ,Rising, Hot, Top, or Controversial, and the subreddit from which want details. The following details will be scrapped from each post: 
'ID', 'Author', 'Title', 'Score', 'Subreddit_Name', 'Url', 'Number_of_Comments', 'Date_Created'.

# How to run?

Run the command: 
```python reddit.py```

# Requirements
- praw==7.1.0
- pandas==1.1.1