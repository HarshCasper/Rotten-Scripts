import pyautogui
import time

a = 0
while a < 4:
    pyautogui.screenshot(
        r"C:\Users\Aryan\Desktop\Screenshot\img"+str(x)+".png")
    a += 1
    time.sleep(2)
