import os

#  Make a file in to store all the environment variables
f = open("env.example","w+")

#  Write the data into the file
for a in os.environ:
    b='Var: ' + a + '\nValue: ' + os.getenv(a) + "\n"
    f.write(b)