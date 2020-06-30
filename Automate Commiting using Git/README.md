# Automate commit using Git

![image](https://steadylearner.com/static/images/post/Python/python-github-by-Steadylearner.png)

Are you tired of adding, commiting and pushing you code everytime you change it? If so, you can use this Python script to automate this boring stuff.
This code is the simplest one to automate the task.

## Understanding the code

![image]()

```
import subprocess
```
The subprocess module allows us to spawn processes, connect to their input/output/error pipes, and obtain their return codes.

```
subprocess.getoutput('git add .')
```
*subprocess.getoutput:* Return output (stdout and stderr) of executing cmd in a shell. That means, it will execute the command ```git add .```

```
message = input("Enter commit message")
```
Now, you can simply understand that we'e taking an input message to give it to the commit message in the next command.

```
subprocess.getoutput('git commit -m ' + message)
```
In this line of code, we can see that the commit message will be appended to the command   ```git commit -m <message>```.

```
branchname = input("Enter branch name")
```
Then, give the branch name to which you want to push your code.

```
subprocess.getoutput('git push origin ' + branchname)
```
Finally, to push our code we are using, ```git push origin <branch-name>```.  
You can also add a variable to the remoteurl for defining the origin, but by default it is origin.



