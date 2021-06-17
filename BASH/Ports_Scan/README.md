# Port_Scan 

Killing ports and process, sounds like a job for Command Line. For that very reason i made a Bash script, 
that first lists out all the process on any port that are _listening_ then gives an option to selectively kill them.

## Important

> Uses `lsof` package.

This package is only available in Linux and Mac. Windows user should prefer this [python_script](https://github.com/HarshCasper/Rotten-Scripts/tree/master/Python/Ports_Scan) I made.

## Setup instructions  

- Install `lsof` package using `apt-get install lsof` or `yum install lsof`
- For running globally, move the file to `/usr/local/bin`
- run `chmod +x ports_scan.sh`
- Now simply run `ports_scan`


## Author(s)  

Made by [Vybhav Chaturvedi](https://www.linkedin.com/in/vybhav-chaturvedi-0ba82614a/)