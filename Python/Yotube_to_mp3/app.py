import tkinter as tk
from tkinter import Entry, StringVar, ttk, messagebox , filedialog
from subprocess import run
import string


floralwhite = '#FFFAF0'                   ## bacground color off app

class downloader():

    def __init__(self):

## creates the main window

        self.win = tk.Tk()
        self.win.geometry("600x150")
        self.win.title("Youtube To Mp3")

## creates the different elements in the window

        self.url = tk.Label(self.win,text= "Video Link",bg=floralwhite,fg='#000000',font= ('Arial',12))
        self.url.grid(row=0,column=0,padx=10,pady=20)
        self.url_entry = tk.Entry(self.win,bg=floralwhite,border=2,width=60)
        self.url_entry.grid(row=0,column=1,padx=5,pady=20)
        self.url_entry.focus_set()

        self.f_path = StringVar()
        self.savelbl = tk.Label(self.win,bg=floralwhite,font = ('Arial',12),fg = '#000000',text = "Save mp3 file")
        self.savelbl.grid(row=1,column=0,padx=5,pady=5)
        self.save_entry = tk.Entry(self.win,bg=floralwhite,border=2,width=60,textvariable=self.f_path)
        self.save_entry.grid(row=1,column=1,padx=10)

## creates the select foleder button
        self.browse_btn = tk.Button(self.win,bg=floralwhite,border=2,text = "Browse",fg="#000000",command=self.browse)
        self.browse_btn.grid(row=1,column=2,padx=5,pady=5)

## creates the download button
        self.submit_btn = tk.Button(self.win,text = "Submit", bg=floralwhite,fg='#000000',border=2,command= lambda : self.submit(self.url_entry.get(),self.save_entry.get()))
        self.submit_btn.grid(row=2,column=1,padx=15,pady=10)

        self.win.configure(bg=floralwhite)
        self.win.mainloop()


    def submit(self,link,path):
        self.url_entry.delete(0,tk.END)
        self.save_entry.delete(0,tk.END)
        self.link = link
        self.path = path

        if self.path != None:
            run(f'youtube-dl --prefer-ffmpeg -o "{self.path}/%(title)s.%(ext)s" --extract-audio --audio-format mp3 {self.link}',
                 shell=True, capture_output=True, text=True).stdout
        else:
             run(f'youtube-dl --prefer-ffmpeg --extract-audio --audio-format mp3 {self.link}',
                 shell=True, capture_output=True, text=True).stdout
        # messagebox.showinfo("Downloader","The video has been converted and downloaded")


    def browse(self):
       self.filename = filedialog.askdirectory()
       self.f_path.set(self.filename)
    


if __name__ == '__main__':
    downloader()