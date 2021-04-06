# Node.js Script to get Active Pull request commentors

---

## About

---

This script written in JavaScript extracts the data like repository's link , pull request Number, link to the pull request, comments on the pull request and username of the coresponding commentors. This script extract data for open PRs only and no. of PR to extract data is handled by user which is 10 by default.

## Explanation of code

- script uses the github GraphQL API https://api.github.com/graphql
- Script make use of **node-fetch** and **csv-writer** node packages
- To the run the script user's has to provide their own github access token, which can be generated using following step:
  - Goto github settings
  - Scroll down to Developer settings
  - click of Personal access tokens
  - click on generate new token
  - give any title and all the permissions
  - Be careful with the token and remember to delete after usual

## How to use the code

---

- Replace the OWNER string with username of owner of repo you want to access the data
- Replace the REPO_NAME with the repository's name you want to access the data
- NO_OF_REQUEST specifies no. of PRs you want the data for.

## Sample Output

![output](https://www.linkpicture.com/q/Screenshot-2021-04-07-at-12.24.33-AM.png)
