from github import Github
import json
import sys
from decouple import config


def RetriveIssueData(storeHere, repoName):
    """The funtion retrives the data of issues and returns an array"""
    issues = repoName.get_issues(state="all")

    for i in issues:
        issue = {}
        issue["Title"] = i.title
        issue["Creator"] = i.user.login
        issue["Assignees"] = [name.login for name in i.assignees]
        issue["OpenedAt"] = i.created_at.strftime("%d-%m-%G")
        if i.closed_at is not None:
            issue["ClosedAt"] = i.closed_at.strftime("%d-%m-%G")
        else:
            issue["ClosedAt"] = None
        if i.pull_request is not None:
            issue["PullRequest"] = i.pull_request.html_url
        else:
            issue["PullRequest"] = None
        issue["Body"] = i.body
        issue["Comments"] = [[j.id, j.user.login] for j in i.get_comments()]
        storeHere.append(issue)

    return storeHere


def RetrivePullRequestData(storeHere, repoName):
    """The funtion retrives the data of PRs and returns an array"""
    PRs = repoName.get_pulls(state="all")

    for i in PRs:
        pr = {}
        pr["ID"] = i.id
        pr["Creator"] = i.user.login
        pr["State"] = i.state
        pr["OpenedAt"] = i.created_at.strftime("%d-%m-%G")
        if i.merged_at is not None:
            pr["MergedAt"] = i.merged_at.strftime("%d-%m-%G")
        else:
            pr["MergedAt"] = None
        if i.closed_at is not None:
            pr["ClosedAt"] = i.closed_at.strftime("%d-%m-%G")
        else:
            pr["ClosedAt"] = None
        rews = []
        for rew in i.get_review_requests():
            for k in rew:
                rews.append([k.id, k.login])
        pr["Body"] = i.body
        pr["Reviewers"] = rews
        pr["FilesChanged"] = i.changed_files
        if i.merged_by is not None:
            pr["MergedBy"] = i.merged_by.login
        else:
            pr["MergedBy"] = None
        storeHere.append(pr)

    return storeHere


def WriteToJSON(data, fileName):
    """This function converts the array of dicts to json and stores it to .json file"""
    with open(str(fileName) + ".json", "w") as file:
        json.dump(data, file, indent=6)
        file.close()
    print("Successfully created " + str(fileName) + ".json")


if __name__ == "__main__":

    # Setup your github token before running the script
    # and set the variable in .env file

    token = config("GITHUBTOKEN")
    g = Github(token)

    # Final info is stored in the following datastructures
    IssuesInfo = []
    PullRequestsInfo = []

    # Getting the repo based on the info from command line
    repo = g.get_repo(str(sys.argv[1]) + "/" + str(sys.argv[2]))

    print("The script may take some time .....")

    # Calling the funtions
    issueData = RetriveIssueData(IssuesInfo, repo)
    WriteToJSON(issueData, "AllIssuesInfo")

    PRData = RetrivePullRequestData(PullRequestsInfo, repo)
    WriteToJSON(PRData, "AllPullRequestsInfo")
