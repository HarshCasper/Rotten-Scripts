# Node Script to get Active Pull request commentors
---

## About

This script written in JavaScript extracts the data like repository's link, pull request Number, link to the pull request, comments on the pull request, and username of the corresponding commentors. This script extracts data for open PRs only and no. of PR to extract data is handled by the user which is 10 by default.

## Explanation of code

- Script uses the GitHub GraphQL API https://api.github.com/graphql
- Script make use of **node-fetch** and **csv-writer** node packages
- To the run the script user's has to provide their own github access token, which can be generated using following step:
  - Goto GitHub settings.
  - Scroll down to the `Developer settings`.
  - Click on the Personal access tokens.
  - Click on `Generate new token`.
  - Give any title and share all the permissions.
  - Be careful with the token and remember to delete after the usual.

## How to use the code
---
- navigate to the folder where script.s file is.
- in terminal or command prompt type - `node script.js OWNER_NAME REPO_NAME NO_OF_REQUEST`
- the order of variables should be same as above

## Sample Output
![output](https://www.linkpicture.com/q/Screenshot-2021-04-07-at-12.24.33-AM.png)
