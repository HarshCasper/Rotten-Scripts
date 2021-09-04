#Necessary Packages
import datetime
import json
import re

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from jupyterthemes import jtplot
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans



#---------------------------------------------------------------------------------------------------------#

"""
This Section contains code block to fetch all the Pull Requests along with title.
The result is zipped to a Pandas DataFrame.
"""
#function to fetch the all Pull Requests along with their links.

def fetch_pr_links(URL):
    """
    Returns the number, title and link of every Pull Request.

    Parameters:
        URL (url) : Url to the Pull Requests page in the repo.
    
    Returns:
        pr_number (list) : All the numbers in a list format.
        pr_title (list) : All the PR titles in a list format.
        pr_links (list) : All the PR links in a list format.

    """
    pr_links=[]
    pr_number=[]
    pr_info=[]
    pr_title=[]
    for x in range(1,30):    # range() --> upper limit value = total number of pages in PR (open + closed) 
        r=requests.get(url=URL)
        soup=BeautifulSoup(r.content,'html.parser')
        div_tags=soup.findAll('div',class_="Box-row Box-row--focus-gray p-0 mt-0 js-navigation-item js-issue-row")
        base_url="https://github.com/"
        for _,i in enumerate(div_tags):
            for a in i.findAll('a'):
                newUrl=base_url+a["href"]
            pr_number.append(_)
            pr_info.append(i.text.strip())
            pr_links.append(newUrl)
    for item in info:
        pr_title.append(re.sub("\n","",item))
    
    return pr_number,pr_title,pr_links


base_url='https://github.com/HarshCasper/Rotten-Scripts/pulls?page=1&q=is%3Apr'
pr_number, pr_title, pr_links = fetch_pr_links(base_url)
    
    

#Converting the fetched information into a Python DataFrame
data=list(zip(pr_number,pr_title,pr_links))
df=pd.DataFrame(data,columns=["No","Info","PR Url"])
for i in range(len(df)):
    df['No'][i]=i


#---------------------------------------------------------------------------------------------------------#

"""
This Section contains the code to fetch status of every Pull Request
and Contributors.
The result is appended to a DataFrame and saved as a CSV file.
"""
#Function to Fetch the status of each and every PR
def pr_status(link):
    """
    Returns the status of every Pull Request.

    Parameters:
        link (url): URL to the every Pull Request.
    
    Returns:
        status (str): Status as a string dtype.

    """
    status=[]
    r=requests.get(url=link)
    soup=BeautifulSoup(r.content,'html.parser')
    div_tags=soup.findAll('div',class_="flex-shrink-0 mb-2 flex-self-start flex-md-self-center")
    for _,i in enumerate(div_tags):
        for span in i.findChild('span'):
            status.append(span)
    status=re.sub('\n','',status[-1])
    status=re.sub(' ','',status)
    return str(status)


# #  Adding 'PR Status' column to the DataFrame
status=[]
for i in range(len(df)):
    print(i)
    status.append(pr_status(df['PR Url'][i]))

df['PR Status']=status


#funtion to fetch the contributors name from each pull request
def pr_names(link):
    """
    Returns all the contributors involved in every PR.

    Parameters:
        link (url): Url of the Pull Request
    
    Returns:
        name (list) : List containing the contributors.

    """
    name=[]
    r=requests.get(url=link)
    soup=BeautifulSoup(r.content,'html.parser')
    div_tags=soup.findAll('div',class_="participation")
    for _,i in enumerate(div_tags):
        for a in i.findAll('a'):
            name.append(re.sub('/' ,"",a['href']))
    return name

pr_contributors=[]

for i in range(len(df)):
    pr_contributors.append(pr_names(df['PR Url'][i]))

df['PR Contributors']=pr_contributors


#Flushing the Pandas DataFrame to a CSV file.
df.to_csv('pr_info.csv')

#---------------------------------------------------------------------------------------------------------#

"""
Bar Plot to show the status count of all the PR's.
"""
#code block to plot a bar graph
colors=['green','red','purple']
plt.figure(figsize=(6,7))
plt.bar(
    ["Open","Closed","Merged"],
    height=[len(df[df['PR Status']=='Open']),len(df[df['PR Status']=='Closed']),len(df[df['PR Status']=='Merged'])],
    width=0.8,
    color=colors,
    zorder=2
)
plt.title('PR Status',fontsize=24)
plt.grid(zorder=1)
plt.show()

#---------------------------------------------------------------------------------------------------------#



"""
This Section contains code for generating unique PR contributors from the the total contributor list.

Along with that,it also contains code for total number of contributions done by every unique contributor
to the repo.

The output is dumped into a JSON file to the current directory.
"""

#This function gets all the names of the contributors by removing all the duplicate values
def pr_contributors_list(lst):
    """
    Returns unique contributors list.

    Parameters: 
        list (list)

    Returns:
        list (list): returning value

    """
    pr_contributors_unique=[]
    for x in lst:
        for y in x:
            if y not in pr_contributors_unique:
                pr_contributors_unique.append(y)
    return pr_contributors_unique
            
pr_contributors_unique=pr_contributors_list(pr_contributors)
print(pr_contributors_unique)

#function to store contributors data into a json file.
def contributors_to_json(pr_contributors,pr_contributors_unique):
    """
    Dumps unique contributors and their total number
    of contributions into a JSON file.

    Parameters:
        pr_contributors (list):
        pr_contributors_unique():

    Returns:
        A JSON file to the current directory.
    
    """
    print("Creating JSON file...")
    pr_contributions={}
    for j in enumerate(pr_contributors_unique):
        SUM=0
        for i in enumerate(pr_contributors):
            count=pr_contributors[i].count(pr_contributors_unique[j])
            SUM+=count
        #print("{}: {}".format(pr_contributors_unique[j],sum))
        pr_contributions[pr_contributors_unique[j]]=sum
    
    with open('Contributors data.json','w') as fp:
        json.dump(pr_contributions,fp)
    
    print("JSON File Created.")

contributors_to_json(pr_contributors,pr_contributors_unique)

#load data from json
def total_contributions_count():
    with open('Contributors data.json') as fp:
        info=json.load(fp)
    return info

info=total_contributions_count()



#---------------------------------------------------------------------------------------------------------#

"""
Bar Plot to show top 5 Contributors.
"""

#code block to show top 5 contributors
colors=['green','r','b','purple','y',]
contributors=list(info.keys())
count=list(info.values())
plt.barh(
    contributors[-5:],
    count[-5:],
    color=colors,
    zorder=2
)
plt.title("Top 5 Contributors",fontsize=25)
plt.xlabel("Count")
plt.ylabel("Contributors")
plt.grid(zorder=1)
for index, value in enumerate(count[-5:]):
    plt.text(value, index,
             str(value))
plt.show()


#---------------------------------------------------------------------------------------------------------#


"""
This Section contains extraction of average time taken by every PR to get merged.
The extracted results are then apppended to a DataFrame and then stored in a csv file.
"""

#creating a "merged_df" dataframe which contains only the rows which are merged PR's
merged_df=df[df['PR Status']=="Merged"]
merged_number_list=df[df['PR Status']=="Merged"]["No"].to_list()


#function to get the date and time history from a merged PR
def datetime_extractor(url):
    """
    Returns start and the end datetime values of a PR.

    Parameters:
        url (url): URL to every Pull Request.

    Returns:
        End (datetime): date and time when the PR was opened for the first time.
        Start (datetime): date and time when the PR was closed.
    """
    datetime=[]
    r=requests.get(url)
    soup=BeautifulSoup(r.content,'html.parser')
    div_tags=soup.findAll('div',class_="TimelineItem-body")
    for _,i in enumerate(div_tags):
        for a in i.findChildren('a'):
            for rt in a.findChildren('relative-time',class_="no-wrap"):
                datetime.append(rt['datetime'])
    return max(datetime),min(datetime)

#function to calculate the time difference of starting and ending time of every merged PR
def merged_pr_active_time(datetime_info):
    """
    Returns the duration of a Pull Request.

    Parameters:
        datetime_info (list): List containing complete timestamps in a Pull Request. 

    Returns:
        timediff (datetime): duration of a Pull Request. 
    """
    datetime_list=[]
    for dates in datetime_info:
        dates=re.sub("T"," ",dates)
        dates=re.sub("Z","",dates)
        dates=re.sub("-","/",dates)
        dates=datetime.datetime.strptime(dates,'%Y/%m/%d %H:%M:%S')
        datetime_list.append(dates)
    maximum=datetime_list[-1]
    minimum=datetime_list[0]
    timediff=maximum-minimum
    return timediff


#list for storing the time difference of starting and ending time of all the merrged PR's
pr_time=[]


#finding out the start and end time of every merged PR and append to "pr_time()"
for i in merged_number_list:
    print(i)
    datetime_info=datetime_extractor(merged_df['PR Url'][i])
    timediff=merged_pr_active_time(datetime_info)
    print(datetime_info)
    pr_time.append(timediff)
    

# adding "Active PR time" values to the dataframe along with "PR Number" column for reference purposes
merged_df['Active PR Time']=pr_time
merged_df['PR No']=df[df["PR Status"]=="Merged"]['No']
merged_df.No=[x for x in range(len(merged_df))]
merged_df=merged_df[['No','PR No', 'PR Url', 'PR Status', 'PR Contributors', 'Active PR Time']]

#calculating the total number of seconds from the "Active PR Time" column
seconds_list=[]
for i in merged_df['PR No']:
    merged_df['Active PR Time'][i]=abs(merged_df['Active PR Time'][i])
    seconds = merged_df['Active PR Time'][i].total_seconds()
    seconds_list.append(abs(seconds))

merged_df['Active time(in Seconds)']=seconds_list

#save all the merged PR's along with new columns into a csv file format
merged_df.to_csv('merged_PR_active_time.csv')


#---------------------------------------------------------------------------------------------------------#



"""
This Section contains the code for finding out active time of Pull Requests using K-Means Clustering.
The obtained result is pushed and saved into a csv file.
"""

model=KMeans(n_clusters=3)
model.fit(np.array(merged_df['Active time(in Seconds)']).reshape(-1,1))
np.random.seed(43)

#to get the centriods of the 3 clusters
print(model.cluster_centers_)

#converting "seconds" to "date hour min sec" format
result=[]
for i in model.cluster_centers_:
    seconds=int(i)
    days=seconds//(24*3600)
    seconds%=(24*3600)
    hours=seconds//3600
    seconds%=3600
    minutes=seconds//60
    seconds%=60
    res="{} days {} hours {} minutes {} seconds".format(days,hours,minutes,seconds)
    result.append(res)
    print(res)

#clustered active PR time 
result.sort()
result=pd.DataFrame(result,columns=["Average PR time"])
print(result)

#save the centroids into a csv file
result.to_csv('average_PR_time(results).csv')


#PR's which have been active more than 80 days
print(merged_df[merged_df['Active time(in Seconds)']>=6915384])


#---------------------------------------------------------------------------------------------------------#
