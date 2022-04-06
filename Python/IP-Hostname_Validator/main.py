import ipaddress
import socket
import sys 

if sys.argv[1]=="ip":
   ip = sys.argv[2]
   try: 
      print(ipaddress.ip_address(ip))
      print('IP Valid')
      host = socket.gethostbyaddr(ip)
      print("Host: " + str(host[0]))
   except ValueError: 
      print('-' *25)
      print('IP is not valid')
   
elif sys.argv[1]=="hostname":
   host = sys.argv[2]
   try:
      print(host)
      # gethostbyname() returns IPv4 address
      ip = socket.gethostbyname(host) 
      print("IP Address: ", ip)
   except socket.gaierror:
      print('-' *25)
      print("Hostname does not exist")
   
      
