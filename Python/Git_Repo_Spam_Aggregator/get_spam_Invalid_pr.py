
from github import Github
from pprint import pprint
import json
from decouple import config


def GetPullData(bucket, repoName):
    """The funtion retrives the Invalid/Spam PR across repositories and returns array"""

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
                # review_requests = GetPrReviewers(pr,repo)
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

    # store Invalid PR content
    PullRequestIDetails = []

    # To store all the content of repositories
    data = []

    # Get the owner i.e username and repository name from the repositories.json file

    with open("repositories.json") as file:
        data = json.load(file)

    # Getting the individual repositories details

    for repo in data:
        repoName = g.get_repo(repo['owner']+"/"+repo['repoName'])
        invalidPRdata = GetPullData(PullRequestIDetails, repoName)

    # Print all the invalid PR data
    print("All the invalid/spam Pr details: ")
    pprint(invalidPRdata)
