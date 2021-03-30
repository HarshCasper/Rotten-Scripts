# GitHub CLI

`pwr` is Pull Requests Workflow on the command line. It brings OPEN, CLOSED,MERGED and other PR concepts to the terminal next to where you are already working with `git` and your code.
`prw` is available for repositories hosted on GitHub.com.

## Setup instructions

<b>it requires a Github Personal Access Token (PAT) to verify the user</b>

| Install:          | Run:                         |
| ----------------- | ---------------------------- |
| `bash install.sh` | `Python prw.py --help`       |
|                   | `python prw.py auth <token>` |

## available commands

- `auth <token> `
- `repo <username/repo_name> [options] [mode] `

## Output

![Screenshot](https://i.imgur.com/jV8qgOG.png)

## Author

<b>[Rahul Raikwar](https://github.com/rahulraikwar00)</i>

## Disclaimers, if any

<i>This script requires a Github Personal Access Token (PAT) to verify the user</i>
<i>It does not have a specialized `upgrade` command yet, but the `install` command should work for upgrading to a newer version of GitHub prw.</i>
