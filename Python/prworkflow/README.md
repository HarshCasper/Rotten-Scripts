# A command line tool for understanding the PR workflow

# setup and run
- run install.sh
```shell
$ bash install.sh
```

## usage:
```shell
$ python -m prworkflow <"username/repo_name"> -<argment> 
``` 

## optional arguments:
```
   prworkflow.py [-h] -u REPONAME [-v] [-pr] [-apr] [-cpr]

  -h, --help                show this help message and exit
  -u REPONAME, --reponame   REPONAME <Required> repository name [username/reponame]
  -v, --verbose             Shows data in verbose mode.
  -pr, --pulls              Totle pull request.
  -apr, --activepr          Active pull request
  -cpr, --closedpr          Closed pull request
```
## Run using 
- example:
```shell
$ python -m prworkflow -u "geekcomputers/Python" -apr
```

#### Note

This Script does not require any specific environment. Simply create your own environment for ML and Data Science pipeline and then run the Script. The Script will do the rest of the work.
