# Python Script to check for Internet Connection

import socket
import os
import time
import subprocess

REMOTE_SERVER = "portal.acttv.in"
def is_connected():
  try:
    print("Checking")
    host = socket.gethostbyname(REMOTE_SERVER)
    s = socket.create_connection((host, 80), 2)
    os.startfile("C:\Windows\Media\Alarm01.wav")
    print("Connected")
  except:
     time.sleep(60)
     print("Net Connection Unavailable")
     is_connected()

is_connected()
