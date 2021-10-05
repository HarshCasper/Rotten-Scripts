__author__ = "Sri Manikanta Palakollu."
__date__ = "22-07-2020"

import socket
import sys
import threading
import queue
import time
from datetime import datetime

# The below commented lines is required when the system has a mutiple python versions Python v2.x and v3.x

"""
try:
    import queue
except:
    import Queue as queue
"""


# Defining Dictionary of common available ports
available_ports = {
    "21": "FTP",
    "22": "SSH",
    "23": "Telnet",
    "25": "SMTP",
    "53": "DNS",
    "67": "DHCP",
    "68": "DHCP",
    "69": "TFTP",
    "80": "HTTP",
    "109": "POPv2",
    "110": "POPv3",
    "123": "NTP",
    "143": "IMAP",
    "194": "IRC",
    "220": "IMAPv3",
    "389": "LDAP",
    "443": "HTTPS",
    "587": "SMTP",
    "993": "IMAPS",
    "994": "IRCS",
    "995": "POP3S",
    "3306": "MySQL",
    "25565": "Minecraft",
}

# Handling the url's properly
if "HTTP" in sys.argv[1].upper():
    if "HTTPS" in sys.argv[1].upper():
        print("Please enter a url without https")
        sys.exit(0)
    else:
        print("Please enter a url without http")
        sys.exit(0)

# printing basic info about the scans
print(
    "\nHost: {}       IP: {}  ".format(sys.argv[1], socket.gethostbyname(sys.argv[1]))
)

# gethostbyname() will give the IPAddress of URL. or it simply performs the DNS Operation.

# returns the value of host , start port and end port


def get_scan_args():
    if len(sys.argv) == 2:
        print("\nStarting Port: {}       Ending Port: {}".format(0, 1024))
        return (sys.argv[1], 0, 1024)
    if len(sys.argv) == 3:
        print("\nStarting Port: {}       Ending Port: {}".format(1, sys.argv[2]))
        return (sys.argv[1], 0, int(sys.argv[2]))
    if len(sys.argv) == 4:
        print(
            "\nStarting Port: {}       Ending Port: {}".format(sys.argv[2], sys.argv[3])
        )
        return (sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))


# tries to establish a connection
def is_port_open(host, port):  # Return boolean
    try:
        # create an INET, STREAMing socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        sock.connect((host, port))
    except socket.error:
        # print("Couldn't connect to server.")
        return False
    return True


def scanner_worker_thread(host):
    while True:
        port = port_queue.get()
        if is_port_open(host, port):
            if str(port) in available_ports:
                print(
                    "Port Number: {}({}) is OPEN!".format(
                        str(port), available_ports[str(port)]
                    )
                )
            else:
                print("Port Number: {} is OPEN!".format(port))
        port_queue.task_done()


scan_args = get_scan_args()
port_queue = queue.Queue()
for i in range(30):
    t = threading.Thread(target=scanner_worker_thread, kwargs={"host": scan_args[0]})
    t.daemon = True
    t.start()

start_time = time.time()
print("Scanning started at %s    \n" % (time.strftime("%H:%M:%S")))
for port in range(scan_args[1], scan_args[2]):
    port_queue.put(port)

port_queue.join()
end_time = time.time()
print("\n\nScanning ended at %s    \n" % (time.strftime("%H:%M:%S")))
print("Scanning completed in {:.3f} seconds.".format(end_time - start_time))
