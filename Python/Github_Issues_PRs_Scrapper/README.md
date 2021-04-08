# Script to fetch all Issues/PRs and store them in a CSV/JSON File

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## The Script fetchs all Issues/PRs and stores them in a JSON File, It ideally works as a handy CLI tool that can allow the maintainers to capture the data trends of the repository

### For the Issues, it capture the following data points

- Issue Creator
- Issue Assignee
- Corresponding PR (if any)
- Issue Open/Close Date
- People who commented on the Issue (Numbers and their Username)
- Issue Content

#### For the PRs capture the following data points

- PR Creator
- Merged/Closed
- PR Open/Close/Merge Date
- Reviewers (Numbers and their Username)
- Who merged the PR?
- PR Content
- Files changed

## Dependencies

 1. python3
 2. PyGithub
 3. json
 4. sys

## Setup instructions

- Install the dependencies using ```pip3 install -r requiremnts.txt```
- Note: You need to generate a githubAPI token and insert(checkout the comments in script) it in the script, To generate the token check this [tutorial](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token)
- You are all set and the [script](master_fetch_script.py) is Ready to run.
- The script takes the username and repo name as the command line argument (refer output).
- Once you run the script, it may take some time to fetch the required data and save it as a .json file.

## Output

- Terminal
[![terminal-OUT.png](https://i.postimg.cc/5NLFRZHb/terminal-OUT.png)](https://postimg.cc/jLq5W3QF)
- AllIssuesInfo.json
[![issuesSS.png](https://i.postimg.cc/7PX3VvTc/issuesSS.png)](https://postimg.cc/JtDHr2xc)
- AllPullRequestsInfo.json
[![prSS.png](https://i.postimg.cc/Qx9FWvgc/prSS.png)](https://postimg.cc/svzjk6N2)

## Author(s)

Made by Jaideep Reddy Kotla

