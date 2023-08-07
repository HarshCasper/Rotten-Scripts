import requests
from bs4 import BeautifulSoup
import csv

page = requests.get('https://github.com/trending')

soup = BeautifulSoup(page.text, 'html.parser')

# get the repo list
repo = soup.find(class_="position-relative container-lg p-responsive pt-6")

repo_list = repo.find_all(class_='Box-row')

# Open writer with name
file_name = "github_trending_today.csv"
# set newline to be '' so that that new rows are appended without skipping any
f = csv.writer(open(file_name, 'w', newline=''))

f.writerow(['Developer', 'Repo Name', 'Programming Language', 'Total Stars', 'Number of Forks'])

for repo in repo_list:
    h1 = repo.find(class_='h3 lh-condensed')
    developer_name = h1.find('span').text.strip().strip(" /")
    repo_name = h1.find('span').next_sibling
    stars = repo.find(class_='octicon octicon-star').next_sibling.text 
    programming_language = repo.find('span', itemprop='programmingLanguage')
    
    if programming_language:
        programming_language=programming_language.text.strip()
    else:
        programming_language=''
    
    no_of_forks = repo.find(class_='octicon octicon-repo-forked').next_sibling.text

    f.writerow([developer_name, repo_name, programming_language, stars, no_of_forks])