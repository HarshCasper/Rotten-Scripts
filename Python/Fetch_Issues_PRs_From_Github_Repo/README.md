# Script to fetch all Issues/PRs and store them in a CSV/JSON File
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
### The Script fetchs all Issues/PRs and stores them in a JSON File. It ideally works as a handy CLI tool that can allow the maintainers to capture the data trends of the repository. 
#### For the Issues, it capture the following data points:
- Issue Creator
- Issue Assignee
- Corresponding PR (if any)
- Issue Open/Close Date
- People who commented on the Issue (Numbers and their Username)
- Issue Content
#### For the PRs capture the following data points:
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
 4. datetime
 5. sys
 <br>
- Note: You need to generate a githubAPI token and insert(checkout the comments in script) it in the script, To generate the token check this [tutorial](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token)
 
 ## Setup instructions

- Install the dependencies using ```pip3 install -r requiremnts.txt```
- You are all set and the [script](master_fetch_script.py) is Ready to run.
- The script takes the username and repo name as the command line argument (refer output).
- Once you run the script, it may take some time to fetch the required data and save it as a .json file.

## Output
- Terminal<br>
![alt text](https://github.com/Jaideep07/Rotten-Scripts/blob/master/Python/Fetch_Issues_PRs_From_Github_Repo/terminalOUT.png?raw=true)
- AllIssuesInfo.json
![alt text](https://github.com/Jaideep07/Rotten-Scripts/blob/master/Python/Fetch_Issues_PRs_From_Github_Repo/issuesSS.png?raw=true)
- AllPullRequestsInfo.json
![alt text](https://github.com/Jaideep07/Rotten-Scripts/blob/master/Python/Fetch_Issues_PRs_From_Github_Repo/prSS.png?raw=true)
## Author(s)

Made by [Jaideep Reddy Kotla](https://www.linkedin.com/in/vybhav-chaturvedi-0ba82614a/)
