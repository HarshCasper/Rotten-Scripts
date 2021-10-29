import psutil
import sys


# To get the PID according to the Port Number
def get_pid():
    connections = psutil.net_connections()
    port = int(sys.argv[1])
    # Using psutil functionality
    for con in connections:
        if con.raddr != ():
            if con.raddr.port == port:
                return con.pid, con.status
        if con.laddr != ():
            if con.laddr.port == port:
                return con.pid, con.status
    return -1


# CLI Input
if __name__ == "__main__":
    if len(sys.argv) > 1:
        pid = get_pid()
        if pid == -1:
            print(":: Not Found :<")
        else:
            print(f"Found service on Port {sys.argv[1]}")
            print(f"[+] PID: {pid[0]}")
            print(f"[+] Status: {pid[1]}")
            ch = input("Close the Port?: (y/n) ")
            # Takes Keyboard Input
            if ch.lower() == "y":
                p = psutil.Process(pid[0])
                p.terminate()
"""
Sample Input - 
python3 ports_kill.py <port number>"""
