import random

def insult():
    a = []
    b = []
    c = []
    a1 = random.randint(0,49)
    b1 = random.randint(0,49)
    c1 = random.randint(0,49)
    with open('insults.txt' ,'r') as file:
        for line in file:
            split_line = line.split()
            a.append(split_line[0])
            b.append(split_line[1])
            c.append(split_line[2])
    return("Thou " + a[a1] + " " +b[b1] + " " + c[c1])


