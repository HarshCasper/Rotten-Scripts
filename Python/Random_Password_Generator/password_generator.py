import string
import random

if __name__ == "__main__":
    # All available LOWERCASE,UPPERCASE,DIGITS AND PUNCTUATION.
    s1=string.ascii_lowercase
    s2=string.ascii_uppercase
    s3=string.digits
    s4=string.punctuation
    #Take input of password length from user
    plen=int(input("Enter Password Length\n"))
    #Make a empty list and extend all elements in the list
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    #Random elements pick from the list S
    random.shuffle(s)
    print("".join(s[0:plen]))
