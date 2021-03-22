import pyautogui
import time
import sys
from datetime import datetime

pyautogui.FAILSAFE = False
numMin = None

# Check if command line argument given, if not then use default 
if ((len(sys.argv)<2) or sys.argv[1].isalpha() or int(sys.argv[1])<1):
    numMin = 1
else:
    numMin = int(sys.argv[1])

# Loop to keep pc awake 
while(True):
    count=0
    # Check for number of minutes to move after
    while(count<numMin):
        time.sleep(60)
        count+=1
    # Move Mouse
    for i in range(0,200):
        pyautogui.moveTo(0,i*4)
    pyautogui.moveTo(1,1)
    # Press Shift
    for i in range(0,3):
        pyautogui.press("shift")
    print("Movement made at {}".format(datetime.now().time()))
    