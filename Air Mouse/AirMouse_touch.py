import socket
import time
from pynput.mouse import Button,Controller
import re


mouse = Controller()

s = socket.socket()         # Create a socket object
host = '192.168.43.173'    #your ip address
port = 5555
s.bind((host, port))


pattern_click = r"n([\w]+)'"
pattern_cursor =r"X=([\b\w\D\.]+)'"
pattern_X = r"X=([\d]+)"
pattern_Y = r"Y=([\d]+)"



def mouse_Action():
      match = re.search(pattern_click,str(url))
      if match:
         print(match.group())
         if "Right" in match.group():
            mouse.click(Button.right)

         elif "Left" in match.group():
             mouse.click(Button.left)


      #Cursor
      match2 = re.search(pattern_cursor,str(url))
      if match2:
         matchx = re.search(pattern_X,match2.group())
         if matchx:
           #print(matchx.group())
           patx = r"([\d]+)"
           x = re.search(patx, matchx.group())
           if x:
              print(x.group())


         matchy = re.search(pattern_Y,match2.group())
         if matchy:
             #print(matchy.group())
             paty = r"([\d]+)"
             y = re.search(paty,matchy.group())
             if y:
                print(y.group())
         mouse.position=(5*int(x.group()),3*int(y.group()))


while True:
   s.listen(5)
   c, addr = s.accept()
   url = c.recv(4800)
  # print(url)
   mouse_Action()
   time.sleep(0)

