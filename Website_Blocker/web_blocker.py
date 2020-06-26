#import the required library
from datetime import datetime as dt

#hosts file path (for Windows)
host_path = "C:\Windows\System32\drivers\etc\hosts"
#Redirects to the localhost
redirect = "127.0.0.1"

#list of all the websites we want to block
website_list = ["facebook.com", "www.facebook.com"]

#Enter the start and end dates for blocking the list of websites
start_date = dt(2020,6,25)
end_date = dt(2020,6,24)
todays_date = dt(dt.now().year, dt.now().month, dt.now().day)


while True:
    #Condition to add the list of websites in the hosts file
    if start_date <= todays_date < end_date:
        with open(host_path,"r+") as file:
            file_text = file.read()
            for site in website_list:
                if site in file_text:
                    pass
                else:
                    #Adds list of websites to be blocked in the host file
                    file.write(redirect + " " + site + "\n")
        print("All sites are BLOCKED. Go and WORK!")
        break
    #When end_date < start_date, the website unblocks
    else:
        #Condition to remove the list of websites from the hosts file
        with open(host_path, "r+") as file:
            content = file.readlines()
            #Bring pointer to the start
            file.seek(0)
            for line in content:
                if not any(site in line for site in website_list):
                    file.write(line)
            #Deletion of file contents from current point to downward
            file.truncate()
        print("All sites are unblocked. Yay! Time to have fun.")
        break
