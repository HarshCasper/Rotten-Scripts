import subprocess
import sys

# Define the full path to Git
GIT_PATH = "/usr/bin/git"

# Stage all changes from the root of the git project
result = subprocess.run([GIT_PATH, "add", ":/"], check=True)
if result.returncode != 0:
    print("Error: Failed to stage changes.")
    sys.exit(1)

# Get commit message from user input or use default value
message = input("Enter commit message (or press Enter to use default): ")
if not message:
    message = "Auto commit"

# Get remote name from user input or use default value
remote = input("Enter remote name (or press Enter to use default 'origin'): ")
if not remote:
    remote = "origin"
    
# Get current branch name
# Get current branch name
branchname = input("Enter branch name (or press Enter to use default 'HEAD'): ")
if not branchname:
    branchname = "HEAD"

# Commit changes
result = subprocess.run([GIT_PATH, "commit", "-m", message],check=True)
if result.returncode != 0:
    print("Error: Failed to commit changes.")
    sys.exit(1)

# Push changes to remote
result = subprocess.run([GIT_PATH, "push", remote, branchname],check=True)
if result.returncode != 0:
    print("Error: Failed to push changes.")
    sys.exit(1)

print("Changes successfully committed and pushed to remote.")

