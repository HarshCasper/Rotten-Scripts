# Find Spam/Invalid Pull Request across GitHub-Repositries

The script retrieves all the spam/invalid Pull Requests from all the Github repositories provided in `repositories.json` and prints in the command line. The script captures the following data points:

For the Pull Request

- Link of the Pull Request
- Pull Request Author
- Number of Files changed
- Number of Pull Request Comments
- Pull Request Reviewer(s)

## Setup instructions

- Install the required dependencies using `pip3 install -r requirements.txt`.
- Generate a `githubAPI` token and add the token to the `.env` file. To generate the token check this [tutorial](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token).
- Add Owner and RepoName to the `repositories.json` file.

```json
Example-
    {
    "owner":"Your-Name",
    "repoName":"Repo-name"
    }
```
- You are all set and the script is Ready to run.
- The script takes the username and repo name from the `repositories.json` files as provided.
- Once you run the script, it may take some time to fetch the required data and prints in command line.

## Output

[![ezgif-com-gif-maker.gif](https://i.postimg.cc/1tWMNmmd/ezgif-com-gif-maker.gif)](https://postimg.cc/LY1jcMZk)

## Author

Made by [Sumit Ghosh](https://github.com/sumitgsh)
