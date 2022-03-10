import tkinter as tk
from tkinter import StringVar,filedialog, messagebox
from subprocess import run
import string


floralwhite = '#FFFAF0'                   ## bacground color off app

def submit(link,path):
    
    if path != None:
        run(f'youtube-dl --prefer-ffmpeg -o "{path}/%(title)s.%(ext)s" --extract-audio --audio-format mp3 {link}',
             shell=True, capture_output=True, text=True).stdout
    else:
         messagebox.showinfo("Downloader", "no link is specified")
            
    url_entry.delete(0,tk.END)
    save_entry.delete(0,tk.END)


def browse(self):
   filename = filedialog.askdirectory()
   f_path.set(filename)
    
## creates the main window

win = tk.Tk()
win.geometry("600x150")
win.title("Youtube To Mp3")

## creates the different elements in the window

url = tk.Label(win,text= "Video Link",bg=floralwhite,fg='#000000',font= ('Arial',12))
url.grid(row=0,column=0,padx=10,pady=20)
url_entry = tk.Entry(win,bg=floralwhite,border=2,width=60)
url_entry.grid(row=0,column=1,padx=5,pady=20)
url_entry.focus_set()

f_path = StringVar()
savelbl = tk.Label(win,bg=floralwhite,font = ('Arial',12),fg = '#000000',text = "Save mp3 file")
savelbl.grid(row=1,column=0,padx=5,pady=5)
save_entry = tk.Entry(win,bg=floralwhite,border=2,width=60,textvariable=f_path)
save_entry.grid(row=1,column=1,padx=10)

## creates the select foleder button
browse_btn = tk.Button(win,bg=floralwhite,border=2,text = "Browse",fg="#000000",command=browse)
browse_btn.grid(row=1,column=2,padx=5,pady=5)

## creates the download button
submit_btn = tk.Button(win,text = "Submit", bg=floralwhite,fg='#000000',border=2,command= lambda : self.submit(url_entry.get(),save_entry.get()))
submit_btn.grid(row=2,column=1,padx=15,pady=10)

win.configure(bg=floralwhite)
win.mainloop()

