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

 - python3
 - PyGithub
 - json
 - sys

## Setup instructions

- Install the dependencies using ```pip3 install -r requirements.txt```
- Note: You need to generate a githubAPI token and insert(checkout the comments in script) it in the script, To generate the token check this [tutorial](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token)
- You are all set and the [script](master_fetch_script.py) is Ready to run.
- The script takes the username and repo name as the command line argument (refer output).
- Once you run the script, it may take some time to fetch the required data and save it as a .json file.

## Output

[![Webp-net-gifmaker-2.gif](https://i.postimg.cc/SN92d9cf/Webp-net-gifmaker-2.gif)](https://postimg.cc/qzkvMzbN)

## Author

Made by [Jaideep Reddy Kotla](https://www.linkedin.com/in/jaideep0707/)

