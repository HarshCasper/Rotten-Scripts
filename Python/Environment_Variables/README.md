# Find Environment Variables

+ This script is used to find all the environment variables used in the code base and write them to an output file.

+ On running this script, all python files are read line by line and matched with regex patterns if any environment variable is get/set.

+ If any match is found, the name of env variable is extracted and stored in a set. Finally, written into an output file.


## To run the script:

```sh
python3 env.py \<codebase path\>
```
