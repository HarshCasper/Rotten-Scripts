# GitHub-Repo Issues and PRs Scrapper

The script retrieves all the vital info of issues and PRs of a given GitHub repo and stores them in a JSON file. The script captures the following data points

For the Issues

- Issue Creator
- Issue Assignee
- Corresponding PR (if any)
- Issue Open/Close Date
- People who commented on the Issue (Numbers and their Username)
- Issue Content

For the PRs

- PR Creator
- Merged/Closed
- PR Open/Close/Merge Date
- Reviewers (Numbers and their Username)
- Who merged the PR?
- PR Content
- Files changed

## Setup instructions

- Install the required dependencies using ```pip3 install -r requirements.txt```
- Generate a `githubAPI` token and create a `.env` file and add the token to it by referring the `.env.example`. To generate the token check this [tutorial](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token)
- You are all set and the [script](master_fetch_script.py) is Ready to run.
- The script takes the username and repo name as the command line argument (refer the output).
- Once you run the script, it may take some time to fetch the required data and save it as a `.json` file.

## Output

[![Webp-net-gifmaker-2.gif](https://i.postimg.cc/SN92d9cf/Webp-net-gifmaker-2.gif)](https://postimg.cc/qzkvMzbN)

## Author

Made by [Jaideep Reddy Kotla](https://www.linkedin.com/in/jaideep0707/)
