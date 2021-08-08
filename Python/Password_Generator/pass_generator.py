# importing the required library
import random

# storing uppercase and lowercase letters in different variables
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()

# storing digits and special characters letters in different variables
digits = "0123456789"
symbols = "@#$%^&*(){}[]./\?-_"

# setting the values to true that we want to use in our passwords 
# if true means we want to use that otherwise not
upper = True
lower = True
numbers = True
special_char = False

# taking a empty string
all_chars = ""

# checking conditions for all variables that we have defined above
if upper:
    all_chars += uppercase_letters
if lower:
    all_chars += lowercase_letters
if numbers:
    all_chars += digits
if special_char:
    all_chars += symbols

# taking the password length and number of passwords that we want
pass_length = 15
no_of_passwords = 10

# with the help of for loop, generating passwords 
for i in range(no_of_passwords):
    password = "".join(random.sample(all_chars, pass_length))
    print(password)
