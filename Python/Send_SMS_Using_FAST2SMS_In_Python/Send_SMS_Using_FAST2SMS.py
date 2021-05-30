import requests
import json
from tkinter.messagebox import showerror, showinfo
from tkinter import *

def send_sms(number, message):
    url = "https://www.fast2sms.com/dev/bulkV2"
    prams ={
        "authorization": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "sender_id" : "TXTIND",
        "route" : "v3",
        "language" : "unicode",
        "numbers" : number,
        "message" : message
    }

    response = requests.get(url, params=prams)
    dic = response.json()
    print(dic)
    return dic.get('return')

def btn_clk():
    num = textNumber.get()
    msg = textMessage.get("1.0", END)
    r = send_sms(num,msg)
    if r:
        showinfo("msg info", "sent successfully")
    else:
        showerror("msg info", "not sent")

root = Tk()
root.title("message sender")
root.geometry("450x550")

photo = PhotoImage (file = "SMS.png")

Label(root, image=photo).grid(row = 0, column =1)
Label(root, text="NUMBER", relief = RIDGE, width = 10).grid(row = 1, column = 0)
textNumber = Entry(root, relief = SUNKEN, font =("Algerian", 20, "bold"), bg = "light yellow", fg = "black", width = 20)
textNumber.grid(row = 1, column = 1)

Label(root, text="MESSAGE", relief = RIDGE, width = 10).grid(row = 3, column = 0)
textMessage = Text(root, relief = SUNKEN, font =("Helvetica", 20, "bold"), height = 10, bg = "blue", fg = "white", width = 20)
textMessage.grid(row = 3, column = 1)

sendbtn = Button(root, text ="SEND", bg="green", fg="white", command=btn_clk).grid(row =4, column =2)
qtbtn = Button(root, text ="QUIT", bg="red", fg="white", command=quit).grid(row =4, column =0)

root.mainloop()
