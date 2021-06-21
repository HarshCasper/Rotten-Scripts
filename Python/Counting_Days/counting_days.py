# import modules like 'os' and 'date'
import os
from datetime import date

# clear the console
if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

print("\nWelcome to Counting Days!\n")

# get the current day
today = date.today()
print("\nCurrent Day: ", today)

# User input for the date
print("\nTell me about the day you wanted...")
try:
    year = int(input("What Year? "))
except ValueError:
    raise ValueError("Invalid Year! You must enter a number for the year.")
try:
    month = int(input("What Month? "))
except ValueError:
    raise ValueError("Invalid Month! You must enter a number for the month.")
try:
    day = int(input("What Day? "))
except ValueError:
    raise ValueError("Invalid Day! You must enter a number for the day.")

# try to build the date object
try:
    futureday = date(year, month, day)
except ValueError:
    raise ValueError("Invalid Date! You must enter a valid date.")

# Display message if date is before today.
if today > futureday:
    raise ValueError("Invalid Date! You must pick a future date.")

# calculate and show date
delta = futureday - today
print("\nThere are", delta.days, "days between", today, "and", futureday, "!")
