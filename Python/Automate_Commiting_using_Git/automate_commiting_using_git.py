import subprocess

# Stage all changes
result = subprocess.run(["git", "add", "."])
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
result = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], capture_output=True, text=True)
if result.returncode != 0:
    print("Error: Failed to get current branch name.")
    exit(1)
branchname = input("Enter branch name (or press Enter to use default '{}'): ".format(result.stdout.strip()))
if not branchname:
    branchname = result.stdout.strip()

# Commit changes
result = subprocess.run(["git", "commit", "-m", message])
if result.returncode != 0:
    print("Error: Failed to commit changes.")
    sys.exit(1)

# Push changes to remote
result = subprocess.run(["git", "push", remote, branchname])
if result.returncode != 0:
    print("Error: Failed to push changes.")
    sys.exit(1)

print("Changes successfully committed and pushed to remote.")

