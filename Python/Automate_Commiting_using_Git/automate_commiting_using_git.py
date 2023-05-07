import subprocess

# Stage all changes
result = subprocess.run(["git", "add", "."])
if result.returncode != 0:
    print("Error: Failed to stage changes.")
    exit(1)

# Get commit message from user input or use default value
message = input("Enter commit message (or press Enter to use default): ")
if not message:
    message = "Auto commit"

# Get remote name from user input or use default value
remote = input("Enter remote name (or press Enter to use default 'origin'): ")
if not remote:
    remote = "origin"

# Get branch name from user input or use default value
branchname = input("Enter branch name (or press Enter to use default 'main'): ")
if not branchname:
    branchname = "main"

# Commit changes
result = subprocess.run(["git", "commit", "-m", message])
if result.returncode != 0:
    print("Error: Failed to commit changes.")
    exit(1)

# Push changes to remote
result = subprocess.run(["git", "push", remote, branchname])
if result.returncode != 0:
    print("Error: Failed to push changes.")
    exit(1)

print("Changes successfully committed and pushed to remote.")

