''' This script will automatically attend zoom meet
'''
import time
import pyautogui

ID = input('Enter Meeting ID: ')
PASSCODE = input('Enter Meeting password: ')
DURATION = input('Enter total duration of meet in seconds')


def autozoom():
    # opening zoom app
    pyautogui.hotkey('alt', 'f2')
    time.sleep(5)
    pyautogui.write('zoom')
    pyautogui.press('enter', interval=0.5)
    time.sleep(5)
    # join button
    x_c, y_c = pyautogui.locateCenterOnScreen('img/join.png', confidence=0.9)
    time.sleep(5)
    pyautogui.click(x_c, y_c)
    # adding ID
    time.sleep(5)
    x_s, y_s = pyautogui.locateCenterOnScreen('img/s3.png', confidence=0.9)
    pyautogui.click(x_s, y_s)
    pyautogui.write(ID)
    # video off
    time.sleep(5)
    x_s, y_s = pyautogui.locateCenterOnScreen('img/s2.png', confidence=0.9)
    pyautogui.click(x_s, y_s)
    # audio off
    time.sleep(5)
    x_s, y_s = pyautogui.locateCenterOnScreen('img/s1.png', confidence=0.9)
    pyautogui.click(x_s, y_s)
    pyautogui.press('enter', interval=5)
    # entering a passcode
    pyautogui.write(PASSCODE)
    pyautogui.press('enter', interval=10)
    print('Hold (Ctrl+c) to exit the program ')

    # Total time of zoom session
    time.sleep(DURATION)

    # closing Zoom
    pyautogui.hotkey('alt', 'f4')
    time.sleep(0.5)
    pyautogui.hotkey('alt', 'f4')


autozoom()
