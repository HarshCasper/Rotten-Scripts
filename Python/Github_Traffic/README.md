# Github_Traffic

This script, can help one determine all the unique viewers on his/her Repository.
By using `access-token` one can determine the viewers and number of time they viewed the Repo.
Currently data of only 14 days is possible (limitation of GitHib-API), but in future by using the GraphQL queries, this limitation can be answered.
Te script uses PickleDB, the data can be imported in CSV as well, although the functionality hasn't been added till this point of time.

## Note

This script can be converted in a Bot, Action or GitHub app!!!


## Dependency

- githubpy
- PickleDB

These are summarised in `requirement.txt`


## Setup

1. A virtual environment (recommended)
1. `pip install -r requirements.txt`
1. Generate your own access token from [here](https://github.com/settings/tokens) (If you already have one with `repo` rights, it can be used as well)
1. It is recommended to paste this token somewhere, as one cant review it again.
1. Determine the Repository whose traffic you want to view.
1. Run the Script

## Usage

Sample Usage -

`
python github_traffic.py collect -u vybhav72954 -r Music-Mood-Analysis -t *********
`

Output -

`
2020-12-20T00:00:00Z {'uniques': 1, 'count': 1}
2020-12-24T00:00:00Z {'uniques': 2, 'count': 17}
2020-12-25T00:00:00Z {'uniques': 1, 'count': 4}
2020-12-27T00:00:00Z {'uniques': 1, 'count': 1}
2020-12-28T00:00:00Z {'uniques': 1, 'count': 23}
2020-12-29T00:00:00Z {'uniques': 1, 'count': 1}
2020-12-30T00:00:00Z {'uniques': 1, 'count': 3}
2020-12-31T00:00:00Z {'uniques': 1, 'count': 7}
`
Generalized Usage -

- collect (Collect Information for first time in Database)

`
python3 github_traffic.py collect -u [github-user] -r [github-repo] -t [github-access-token]
`

- view (View Information already stored in Database)

`
python3 github_traffic.py view -u [github-user] -r [github-repo] -t [github-access-token]
`

`
2020-12-20T00:00:00Z {"uniques": 1, "count": 1}
2020-12-24T00:00:00Z {"uniques": 2, "count": 17}
2020-12-25T00:00:00Z {"uniques": 1, "count": 4}
2020-12-27T00:00:00Z {"uniques": 1, "count": 1}
2020-12-28T00:00:00Z {"uniques": 1, "count": 23}
2020-12-29T00:00:00Z {"uniques": 1, "count": 1}
2020-12-30T00:00:00Z {"uniques": 1, "count": 3}
2020-12-31T00:00:00Z {"uniques": 1, "count": 7}
8 elements
`

## Disclaimer

- `githubpy` is a 8 year old package and is no longer maintained
- Inspired by [this](https://github.com/seladb/github-traffic-stats/blob/master/README.md)


## Author(s)  

Made by [Vybhav Chaturvedi](https://www.linkedin.com/in/vybhav-chaturvedi-0ba82614a/)

