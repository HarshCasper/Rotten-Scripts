import subprocess
subprocess.getoutput('git add .')
message = input("Enter commit message")
subprocess.getoutput('git commit -m ' + message)
branchname = input("Enter branch name")
subprocess.getoutput('git push origin ' + branchname)