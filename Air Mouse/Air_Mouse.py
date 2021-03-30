from pynput.mouse import Button,Controller
import socket
import bs4
import time
import math

ip = '192.168.1.17'
port = 5555
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((ip,port))
oldz = 9
mouse = Controller()

def sensor_data():
    sauce = bs4.BeautifulSoup(data,'lxml')
    x = sauce.find('accelerometer1')
    X = int(float(x.text))
    y = sauce.find('accelerometer2')
    Y = int(float(y.text))
    z = sauce.find('accelerometer3')
    Z = int(float(z.text))
    print('X: ' + str(X))
    print('Y: ' + str(Y))
    print('Z: ' + str(Z))
    single_click = sauce.find('lightintensity')
    mouse.move(-X*6,Y*6)

    #left click
    if int(float(single_click.text)) <= 10:
        mouse.click(Button.left)
        mouse.release(Button.left)
        print("Left Click")

    #right click
    if oldz > Z:
        if oldz - Z > 2:
            mouse.click(Button.right)
            mouse.release(Button.right)
            print("Right Click")
    else:
        saveold()
        
def saveold():
    sauce = bs4.BeautifulSoup(data,'lxml')
    z = sauce.find('accelerometer3')
    Z = int(float(z.text))
    oldz = Z
    
while True:
    rawdata = sock.recvfrom(port)
    data = str(rawdata)
    sensor_data()
    time.sleep(0)
