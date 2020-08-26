#Imports
import random

#Shakesperean Insults are generated in this module
#The file insults_content.txt consists of 3 columns of words.
#A random word is chosen from each of the columns and returned.

def insult():
    subject = []
    predicate = []
    verb = []
    with open('insults_content.txt' ,'r') as file:
        for line in file:
            split_line = line.split()
            subject.append(split_line[0])
            predicate.append(split_line[1])
            verb.append(split_line[2])
    return("Thou art a " + random.choice(subject) + " " + random.choice(predicate) + " " + random.choice(predicate))

if __name__ == "__main__":

    print(insult())

