import os, shutil, sys, instaloader
from prettytable import PrettyTable
instagramBot = instaloader.Instaloader(quiet = True)

def auth():
    # Inputting the Username of User
    userName = input("Enter Your Instagram Username: ")
    try:
        # Try  getting auth credentials from pre-saved files
        instagramBot.load_session_from_file(userName)
    except:
        try:
            # Make the auth credentials
            os.system("instaloader -l {0}".format(userName))
            instagramBot.load_session_from_file(userName)
        except:
            # Login in the account
            instagramBot.login(userName,input("Enter Password: "))
            instagramBot.save_session_to_file()
    print("{0} Logged In.".format(userName))

def main():
    # Login
    auth()
    # While Loop so Script does not exit
    while True:
        # Printing the Tasks
        print("Indexes and Tasks")
        myTable = PrettyTable(["Index","Task"])
        myTable.add_row(["1", "Download Profile Image from Username"])
        myTable.add_row(["2", "Download All Posts from Username"])
        myTable.add_row(["3", "Download Images from Hashtags"])
        print(myTable)
        # Inputting what to do
        query = input("Enter Index to Perform: ")
        # Download Profile Picture case
        if query == "1":
            currentPath = os.getcwd()
            username = input("Enter Username to Download Profile Image: ")
            instagramBot.download_profile(username, profile_pic_only = True)
            for file in os.listdir(username):
                if ".jpg" in file:
                    shutil.move("{0}/{1}".format(username,file),currentPath)
            shutil.rmtree(username)
            print("'{0}' Profile Image Downloaded.".format(username))
        # Download all Photos and Videos
        elif query == "2":
            currentPath = os.getcwd()
            username = input("Enter Username to Download: ")
            try : 
                profile = instaloader.Profile.from_username(instagramBot.context, username)
            except:
                print("Username Not Found.")
            if os.path.exists(username) is False:
                os.mkdir(username)
            os.chdir(username)
            if os.path.exists("Videos") is False:
                os.mkdir("Videos")
            posts = profile.get_posts()
            print("Downloading... Ctrl + C to Stop in between. Don't Open Username Folder.")
            for index, post in enumerate(posts):
                try:
                    instagramBot.download_post(post, target = index)
                except KeyboardInterrupt:
                    print("Downloader Exited.")
                    break
            # Organizing the Directory
            for folder in os.listdir():
                if "." not in folder:
                    for item in os.listdir(folder):
                        if ".jpg" in item:
                            shutil.move(folder+"/"+item, "{0}/{1}".format(currentPath, username))
                        elif ".mp4" in item:
                            try:
                                shutil.move(folder+"/"+item, "{0}/{1}/Videos".format(currentPath, username))
                            except:
                                continue
                    shutil.rmtree(folder)
            print("{} Folder Created.".format(username))
        # Download Images using hashtag
        elif query == "3":
            try:
                instaloader.Instaloader(download_videos=False, save_metadata=False, post_metadata_txt_pattern='').download_hashtag(input("Enter Hashtag: "), max_count=20)
            except KeyboardInterrupt:
                print("Downloader Exited")
if __name__ == "__main__":
    main()
