import  youtube_dl
import os

def download():                                                                        # main download function to download and convert
    video_url = input("Enter youtube url: ")                                           # enter he video url
    video_info = youtube_dl.YoutubeDL().extract_info(url = video_url,download=False)
    base = os.path.expanduser('~')                                                      # gets the default user path 
    redo =True
    while redo:

        file_dir = input("enter path to save the downloaded file(q to save in default location): ")
        if file_dir == 'q':
            file_dir = base + "\\Desktop"

        elif os.path.exists(file_dir):                                                   # validates weather input path is valid or not
            redo = False 

    file_name = f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':file_dir + "\\" + file_name,
    }
 
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    print("download completed!!!.")


if __name__ == '__main__':                                                            # main function
    download()