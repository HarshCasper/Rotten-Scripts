from selenium import webdriver
import mycontacts
import tkinter as tk
from tkinter import *

screen = tk.Tk(screenName="WhatsappBomber App")
screen.geometry("1600x640")
screen.title("WhatsApp SMS Bomber")
screen.configure(bg="#1A1A1D")


def sendmessg():
    driver= webdriver.Chrome()
    d1= driver.get("https://web.whatsapp.com/")
    driver.maximize_window()

    return

#Creating a Banner for the main Screen using Label and positioning it on the screen using grid
banner = Label(screen, text= "Whatsapp SMS BOMBER", height = 3, width= 100, bg= "#1A1A1D", fg= "#c3073f")
banner.grid(row=0, column = 0, columnspan=10)
banner.config(font=("Libre Baskerville", 20))

#Creating a name,message,countofmsg for the main Screen using Label and positioning it on the screen using grid
name =  Label(screen, text= "Select the contacts you want to send message", height = 2, width = 40, bg="#4E4E50", fg= "#950740")
message =  Label(screen, text= "Type in your message", height = 2, width = 40, bg="#4E4E50", fg= "#950740")
countofmesg =  Label(screen, text= "select the count of messages to be sent", height = 2, width = 40, bg="#4E4E50", fg= "#950740")

name.grid(row = 1, column= 0, pady = 10)
message.grid(row = 5, column= 0, pady = 10)
countofmesg.grid(row = 6, column= 0, pady = 10)

#Dyanamically creating checkboxes from the list of contacts of the sender and positioning it on the screen
le=len(mycontacts.my_contacts)
listcheck=[None]*le
k=1
col=1
for i in range (0,le):
    listcheck[i]=StringVar()
    a=Checkbutton(screen, text=mycontacts.my_contacts[i], variable=listcheck[i], onvalue=mycontacts.my_contacts[i], offvalue="",  width =20)
    if(col<=4):
        a.grid(row=k, column= col, pady=5)
        col+=1
    else:
        k+=1
        col=1
        a.grid(row=k, column= col, pady=5)
        col+=1
message_entry = Entry(width= 100)
count_entry = Entry(width= 100)

#Positioning the entry boxes for the message and count
message_entry.grid(row = 5, column = 1,pady=10, ipady=6,columnspan=2)
count_entry.grid(row = 6, column = 1, pady=10, ipady=6, columnspan=2)


send_now = Button(screen, text="Send Now", command = sendmessg, width= 40, bg="#6F2232", fg= "#000000")
send_now.grid(row =8, column = 2, ipady=6, pady=10)

screen.mainloop()