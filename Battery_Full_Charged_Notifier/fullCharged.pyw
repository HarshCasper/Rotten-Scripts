import psutil #Library to get System details
import time
import pyttsx3 # Library for text to speech Offline
from win10toast import ToastNotifier # also need to install win32api (This is for Notifications)
import threading # To make notification and speech work at same time

toaster = ToastNotifier()
x=pyttsx3.init()
x.setProperty('rate',130)
x.setProperty('volume',8)
count = 0

def show_notification(show_text):
   toaster.show_toast(show_text,
                       icon_path='battery.ico',
                       duration=10)
   # loop the toaster over some period of time
   while toaster.notification_active():
      time.sleep(0.1)

def monitor():
   while (True):
      time.sleep(10)
      battery = psutil.sensors_battery()
      plugged = battery.power_plugged
      percent = int(battery.percent)

      if percent == 100:
         if plugged == True:
            processThread = threading.Thread(target=show_notification, args=("Laptop Fully Charged",))  # <- note extra ','
            processThread.start()
            x.say("Laptop is Fully Charged Please plug out the cable")
            x.runAndWait()
      elif percent == 90:
         if plugged == True:
            if count == 0:
               processThread = threading.Thread(target=show_notification, args=("Your Battery at 90% Please plug out the cable",))  # <- note extra ','
               processThread.start()
               x.say("Your battery at 90% ")
               x.runAndWait()
               count = count + 1

if __name__ == "__main__":
   monitor()