import tkinter as tk
import speedtest
from tkinter import messagebox

st = speedtest.Speedtest()
root = tk.Tk()
root.geometry("400x400")
root.title("SpeedTest")
root.config(bg="#3b4d61")
font = ("Verdana",15, "bold")

def check():
    messagebox.showinfo("Confirmation", '''Speed Test Starting ..... 
                                            It may take upto 1 min''')
    d.configure(text=str(st.download()//10**6)+"Mbps")
    u.configure(text=str(st.upload()//10**6)+"Mbps")
    p.configure(text=str(int(st.results.ping))+"MS")
    l.configure(text="Speed Test Complete")
    
dspeed = tk.Label(root,text="Download Speed:",bg="#3b4d61",fg="yellow",font=font)
dspeed.place(x=10,y=10)
d = tk.Label(root,text="0 Mbps",bg="#3b4d61",fg="yellow",font=font)
d.place(x=250,y=10)
uspeed = tk.Label(root,text="Upload Speed:",bg="#3b4d61",fg="yellow",font=font)
uspeed.place(x=10,y=50)
u = tk.Label(root,text="0 Mbps",bg="#3b4d61",fg="yellow",font=font)
u.place(x=250,y=50)
ping = tk.Label(root,text="Ping:",bg="#3b4d61",fg="yellow",font=font)
ping.place(x=10,y=90)
p = tk.Label(root,text="0 MS",bg="#3b4d61",fg="yellow",font=font)
p.place(x=250,y=90)

l = tk.Label(root,text="Click Here to start speed test",bg="#3b4d61",fg="yellow",font=(15))
l.place(x=50,y=250)
b = tk.Button(root,text="Speed Text",command=check,bg="yellow",fg="black")
b.place(x=50,y=300,height=40,width=300)
root.mainloop()