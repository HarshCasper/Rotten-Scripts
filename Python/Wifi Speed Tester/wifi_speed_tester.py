# importing requiered modules
import win10toast
import speedtest

st = speedtest.Speedtest() 
download = st.download()/1048576                                                                 #download speed
upload = st.upload()/1048576                                                                     #upload speed
servernames =[]
names = st.get_servers(servernames)
ping = st.results.ping                                                                           #ping
data = [download,upload,ping]                                                                    #storing the values in a list
formated_data = ['%.2f' % elem for elem in data]    
message = 'Download Speed: {}Mbps, \nUpload Speed: {}Mbps,\n Ping: {}ms'.format(*formated_data)  #creating a message for the notification
toaster = win10toast.ToastNotifier()                                                             #creating a notification window                 
toaster.show_toast('Wifi Speedtest Successfull!', message, duration=10)                          #displaying the notification
print(message)                                                                                   #printing the data