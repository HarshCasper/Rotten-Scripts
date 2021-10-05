import os
import sys
import virtualenv

print("Project Name:")
name = input()
print("Directory(Valid) to store the project:")
loc = input()
# if invalid directory, stops the program
if os.path.isdir(loc) is not True:
    print("Invalid Directory")
    sys.exit()

os.chdir(loc)
os.makedirs(name)
loc = loc + "/" + name
os.chdir(loc)
sys.argv = [sys.argv[0], "env"]
# creates a virtualenv with the name env
virtualenv.cli_run({sys.argv[1]})
open("run.py", "a").close()
open("config.py", "a").close()
commands = ["app", "instance", "app/static", "app/templates"]
for i in commands:
    os.makedirs(i)
os.chdir(loc + "/app")
open("__init__.py", "a").close()
