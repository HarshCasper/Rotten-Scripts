# Fetch contributions

- Script can be executed as a CLI.
- Takes arguments username and organization.
- Returns the pull requests made by user to the organization into a Markdown file. 	
	- Markdown file consists a table having - "Title to PR" , "Link of PR" , "Status(Merged/Closed/Open)"

## Example Markdown File:

|    | Title to PR                                               | Link of PR                                                            | Status(Merged/Closed/Open)   |
|---:|:----------------------------------------------------------|:----------------------------------------------------------------------|:-----------------------------|
|  0 | Format Code using Black                                   | https://github.com/moja-global/FLINT.Cloud/pull/22                    | Merged                       |
|  1 | Governance refactor                                       | https://github.com/moja-global/About_moja_global/pull/134             | Merged                       |
|  2 | Refactored Branding Guidelines                            | https://github.com/moja-global/About_moja_global/pull/133             | Merged                       |
|  3 | CI: Add Stale, Request Info and Prosebot                  | https://github.com/moja-global/About_moja_global/pull/132             | Merged                       |
|  4 | Refactoring the Contribution Docs                         | https://github.com/moja-global/About_moja_global/pull/130             | Merged                       |
|  5 | Fix the README                                            | https://github.com/moja-global/About_moja_global/pull/129             | Merged                       |
|  6 | Add Issue Template configuration                          | https://github.com/moja-global/About_moja_global/pull/124             | Merged                       |
|  7 | CI: Add Stale, Request Info and Prosebot                  | https://github.com/moja-global/FLINT_Modules_docs/pull/6              | Merged                       |
|  8 | Add beginner module documentation                         | https://github.com/moja-global/Google_Season_of_Documentation/pull/23 | Merged                       |
|  9 | Add Documentation Working Group Proposal                  | https://github.com/moja-global/Google_Season_of_Documentation/pull/20 | Merged                       |
| 10 | Update README.md                                          | https://github.com/moja-global/FLINT-JSON-Interface/pull/40           | Merged                       |
| 11 | Fixed multiple import name                                | https://github.com/moja-global/FLINT.Data_Preprocessing/pull/7        | Merged                       |
| 12 | CI: Add Pull Request Template, Stale and Request Info Bot | https://github.com/moja-global/FLINT/pull/105                         | Open                         |
| 13 | Refactor Directory Structure                              | https://github.com/moja-global/contributors_website/pull/9            | Merged                       |



## Setup Instructions:
The Code is written in Python 3.9. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). 
```bash
git clone https://github.com/kadatatlukishore/Rotten-Scripts.git
cd Python/Fetch_contributions/
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python3 fetch_contributions.py --username <Username> --organization <Organization>

Example: 
>>> python3 fetch_contributions.py --username <HarshCasper> --organization moja-global
 
```
We will get the resuts in a file like **above** table.