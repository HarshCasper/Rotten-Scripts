import psutil
import sys

def get_pid():
    connections = psutil.net_connections()
    port = int(sys.argv[1])
    for con in connections:
        if con.raddr != tuple():
            if con.raddr.port == port:
                return con.pid, con.status
        if con.laddr != tuple():
            if con.laddr.port == port:
                return con.pid, con.status
    return -1

if __name__ == '__main__':
    if len(sys.argv) > 1:
        pid = get_pid()
        if pid == -1:
            print(":: Not Found :<")
        else:
            print(f"Found service on Port {sys.argv[1]}")
            print(f"[+] PID: {pid[0]}")
            print(f"[+] Status: {pid[1]}")
            ch = input("Wanna Close: (y/n) ")
            if ch.lower() == 'y':
                p = psutil.Process(pid[0])
                p.terminate()
