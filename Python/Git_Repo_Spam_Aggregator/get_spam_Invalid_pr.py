
from github import Github
from pprint import pprint
import json
from decouple import config
from github.GithubException import GithubException


def GetPullData(bucket, repoName):
    """The funtion retrives the Invalid/Spam Pull Request across repositories and returns array"""

    bucket = []
    pulls = repoName.get_pulls(state='closed')
    # loop through pulls to get the pull labels
    for i in pulls:
        for label in i.labels:
            if label.name == "invalid" or label.name == "spam":
                # if invalid
                pr = {}
                pr['Link'] = i.url
                pr['Author'] = i.user.login
                pr['FilesChanged'] = i.changed_files
                pr['Comments'] = i.comments

                reviewers = []
                for rvrs in i.get_review_requests():
                    for k in rvrs:
                        reviewers.append(k.login)
                pr["Reviewers"] = reviewers

                bucket.append(pr)

    return bucket


if __name__ == "__main__":

    # Setup your github token before running the script
    # and set the token in .env file
    # Add repositories to the json file

    token = config("GITHUB_TOKEN")
    g = Github(token)

    # store Pull Request Details content
    PullRequestIDetails = []

    # store Invalid Pull Request(s) content
    invalidPRdata = []

    # store all the content of repositories
    data = []

    # Get the owner i.e username and repository name from the repositories.json file

    with open("repositories.json") as file:
        try:
            data = json.load(file)

            if(len(data)>0):
                # Getting the individual repositories details
                for repo in data:
                    repoName = g.get_repo(repo['owner']+"/"+repo['repoName'])
                    invalidPRdata = GetPullData(PullRequestIDetails, repoName)
                    print(repoName)
            else:
                print("The repository.json file is Empty")

        # when repository does not exist
        except GithubException as e:
            if (e.data['message']=='Not Found'):
                print("The provided Repository does not exist") 

    print("All the invalid/spam Pull Request(s) details: ")
    pprint(invalidPRdata)
