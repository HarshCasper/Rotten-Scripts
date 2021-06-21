import re, os, glob, sys

# the directory path of codebase
path = sys.argv[1]

# regex pattern to set/get environment variables in python
patternSet = r"os.environ\['[a-zA-Z0-9]+'\]"
patternGet = r"os.environ.get\('[a-zA-Z0-9]+'\)"

# set to store unique environment variables used
environmentVariables = set()

# for all python files in the codebase
for file in glob.glob(path + "*.py"):
    # open the python file
    filePtr = open(file, "r")
    # read all its content
    code = filePtr.readlines()

    # match each code line to the patterns defined
    for sequence in code:
        if re.search(patternSet, sequence):
            # extract env name according to set pattern after spliting the string
            env = sequence.split("['")[1].split("']")[0]
            environmentVariables.add(env)

        if re.search(patternGet, sequence):
            # extract env name according to get pattern after spliting the string
            env = sequence.split("get('")[1].split("')")[0]
            environmentVariables.add(env)

# open the file to store output
fout = open("./Environment_Variables.txt", "w")
environmentVariables = list(environmentVariables)
# write all environment variables in the output file
for env in environmentVariables:
    fout.write(env)
