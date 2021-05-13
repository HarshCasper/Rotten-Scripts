# Environment Variables

Environment variables contain information about your login session, stored for the system shell to use when executing commands. They exist whether you’re using Linux, Mac, or Windows.

Use cases for environment variables include but are not limited to data such as:
+ Execution mode (e.g., production, development, staging, etc.)
+ Domain names
+ API URL/URI’s
+ Public and private authentication keys (only secure in server applications)
+ Group mail addresses, such as those for marketing, support, sales, etc.
+ Service account names


# Find Environment Variables in Python Program

+ This script is used to find all the environment variables used in the code base and write them to an output file.

+ On running this script, all python files are read line by line and matched with regex patterns if any environment variable is get/set.

+ If any match is found, the name of env variable is extracted and stored in a set. Finally, written into an output file.

![alt text](https://appdividend.com/wp-content/uploads/2019/11/How-To-Set-Environment-Variables-In-Python.png)

## To run the script:

```sh
python3 env.py \<codebase path\>
```
