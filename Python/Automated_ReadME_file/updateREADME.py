import os

def getListDir():
    # get all the directories and ignoring hidden files.
    dirList = [dir for dir in os.listdir('.') if os.path.isdir(dir) if dir[0]!='.'] 
    return dirList

def defineHeader(README):
    # README Heading for the directory.
    mdFile = open(README,'w')
    mdFile.write('## All the projects in this Directory:\n')
    mdFile.close


def updateREADME(README):
    defineHeader(README)
    dir_list = getListDir()
    mdFile = open(README,'a')
    for dir in dir_list:
        mdFile.write('- ['+dir+'](./'+dir+')\n')
    mdFile.close


# ReadME filename : 
README = 'AutomatedREADME.md'
updateREADME(README)
