# Email Scraper for commit history

A simple python script to crawl all email address, name and username from a specific repository on GitHub.

## Setup instructions

<b>it requires a Github Personal Access Token (PAT) to verify the user</b>

| Install:          | Run:                                    |
| ----------------- | --------------------------------------- |
| `bash install.sh` | `Python email_scrape.py --help`         |
|                   | `python email_scrape.py <token> <repo>` |

## Author

<b>[Rahul Raikwar](https://github.com/rahulraikwar00)</i>

## Disclaimers, if any

- <i>This script requires a Github Personal Access Token (PAT) to verify the user</i>
- <i>It does not have a specialized `upgrade` command yet, but the `install` command should work for upgrading to a newer version of GitHub prw.</i>
- <i>It do not store your Github Personal Access Token (PAT)</i>
