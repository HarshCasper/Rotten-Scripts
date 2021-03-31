#importing the modules
from playsound import playsound
import time
import datetime

# Taking the user inputs of the time when the alarm will sound
day = input("Enter the day ")
month = input("Enter the month ")
year = input("Enter the year ")
hour = input("Enter the time ")
minute = input("Enter the minute")

# creating the scheduled date
sch_date = datetime.date(int(year),int(month),int(day))

loop_var = 1

# creating an infinite while loop
while loop_var > 0:
    # checking whether the time given by the user matches with the time of the system
    if time.localtime().tm_hour == int(hour) and time.localtime().tm_min == int(minute) and datetime.date.today() == sch_date:
        playsound('alarm.wav')
        break
    #if not incresase the variable
    else:
        loop_var += 1
        