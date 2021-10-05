import os
import sys


def main():
    x = input("1. Shutdown\n2. Cancel\n3. Close\n")
    if x == "1":
        shutdown()
    elif x == "2":
        cancel()
    elif x == "3":
        sys.exit()
    else:
        print("Invalid! option")


def cancel():
    command("shutdown -a")


def shutdown():
    t = int(input("how long to shut down the computer:\n"))
    t = str(t * 60)
    cmd = "shutdown -s -f -t " + t
    command(cmd)


def command(cmd):
    os.system(cmd)


if __name__ == "__main__":
    main()
