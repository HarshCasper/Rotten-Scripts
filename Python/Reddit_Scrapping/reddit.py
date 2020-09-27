import praw
import pandas as pd
import datetime as dt

print("Enter the following: ")
client_id = input("Enter your client ID of Reddit app: ")
client_secret = input("Enter your client secret of Reddit app: ")
user_agent = input("Enter user agent: ")
subreddit = input("Enter the subreddit you want to scrape (Ex: Politics, COVID, etc): ")
limit = int(input("Enter how many post you want from each subreddit: "))
type_of_post = input("Enter the catergory of post you want to scrape (new, rising, hot, top, or controversial): ")


reddit = praw.Reddit(client_id=client_id, 
                    client_secret=client_secret,
                    user_agent=user_agent)

data = []

if type_of_post == 'hot':
    posts = reddit.subreddit(subreddit).hot(limit=limit)
elif type_of_post == 'new':
    posts = reddit.subreddit(subreddit).new(limit=limit)
elif type_of_post == 'rising':
    posts = reddit.subreddit(subreddit).rising(limit=limit)
elif type_of_post == 'top':
    posts = reddit.subreddit(subreddit).top(limit=limit)
elif type_of_post == 'controversial':
    posts = reddit.subreddit(subreddit).controversial(limit=limit)
else:
    print("Wrong Type of post selected!")

for post in posts:
    data.append([post.author, post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.created])
        
posts = pd.DataFrame(data ,columns=['author', 'title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'created'])
posts['Date'] = posts.Date.apply(lambda x: dt.datetime.fromtimestamp(x))
posts.to_csv('result.csv') 
print("For results take a look at result.csv")