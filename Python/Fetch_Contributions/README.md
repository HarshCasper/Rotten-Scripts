# Fetch contributions

- Script can be executed as a CLI.
- Takes arguments username and organization.
- Returns the pull requests made by user to the organization into a Markdown file. 	
	- Markdown file consists a table having - "Title to PR" , "Link of PR" , "Status(Merged/Closed/Open)"

## Example Markdown File:

|    | Title to PR                                               | Link of PR                                                            | Status(Merged/Closed/Open)   |
|---:|:----------------------------------------------------------|:----------------------------------------------------------------------|:-----------------------------|
|  0 | Format Code using Black                                   | https://github.com/moja-global/FLINT.Cloud/pull/22                    | Merged                       |

See [Here](https://github.com/kadatatlukishore/Rotten-Scripts/blob/fetch-pullrequests/Python/Fetch_Contributions/markdown_file.md)



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
>>> python3 fetch_contributions.py --username HarshCasper --organization moja-global
 
```
We will get the resuts in a file like **above** table.

# AUTHOR 
**K Kishore**
