import subprocess as sp
print(''' Enter your choice-
        1. add files
        2. commit files
        3. push to the repository
        4. to check the existing remote
        5. pull from the repository
        6. check status
        7. Initialize git
        8. change directory
        '''
)
while True:
    choice = input('Enter your choice-')
    if choice == '1':
        print(sp.getoutput('git add .'))
    elif choice == '2':
        message = input('enter commit message')
        print(sp.getoutput('git commit -m ' + message))
    elif choice == '3':
        print(sp.getoutput('git push origin master'))
    elif choice == '4':
        print(sp.getoutput('git remote -v'))
    elif choice == '5':
        print(sp.getoutput('git pull'))
    elif choice == '6':
        print(sp.getoutput('git status'))
    elif choice == '7':
        print(sp.getoutput('git init'))
    elif choice == '8':
        print('Present working directory')
        print(sp.getoutput('pwd'))
        direc = input('enter the directory you wanna switch')
        print(sp.getoutput('cd ' + direc))
    else:
        print('wrong choice')