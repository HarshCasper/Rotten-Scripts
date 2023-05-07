# Automate commit using Git


Are you tired of adding, committing and pushing you code everytime you change it? If so, you can use this Python script to automate this boring stuff.
This code is the simplest one to automate the task.

## Understanding the code

![image](https://snipboard.io/cM59xz.jpg)

```
import subprocess
```

The subprocess module allows us to spawn processes, connect to their input/output/error pipes, and obtain their return codes.

```
result = subprocess.run(["git", "add", "."])

```

This line of code stages all changes made to files in the current directory using the `git add` command.

```
message = input("Enter commit message (or press Enter to use default): ")

```

This line of code prompts the user to enter a commit message. If the user enters nothing and presses Enter, the commit message will default to "Auto commit".

```
remote = input("Enter remote name (or press Enter to use default 'origin'): ")

```

This line of code prompts the user to enter a remote name for the repository. If the user enters nothing and presses Enter, the remote name will default to "origin".

```
branchname = input("Enter branch name (or press Enter to use default 'main'): ")

```

This line of code prompts the user to enter a branch name to which the changes should be pushed. If the user enters nothing and presses Enter, the branch name will default to "main".

```
result = subprocess.run(["git", "commit", "-m", message])

```
This line of code commits the staged changes using the commit message provided by the user (or the default message, if none was provided).

```
result = subprocess.run(["git", "push", remote, branchname])

```
Finally, this line of code pushes the committed changes to the specified branch and remote.

## Usage

To use this script, simply run it in the directory where your git repository is located. Follow the prompts to enter a commit message, remote name, and branch name, or press Enter to accept the defaults.
## Note
> This script assumes that you have already initialized a git repository in the directory where it is being run. If you have not done so, you will need to initialize a git repository using git init before using this script.
