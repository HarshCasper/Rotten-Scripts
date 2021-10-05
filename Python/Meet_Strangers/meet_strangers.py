# Python Script to spot strangers on a Public WiFi Network by scrapping their MAC Addresses and storing them in a Text File
import sys
from os import path
from re import compile, findall
from subprocess import Popen, PIPE
from colorama import init, Fore, Back, Style

init(autoreset=True)


def get_clipboard_data():
    p = Popen(["pbpaste"], stdout=PIPE)
    p.wait()
    data = str(p.stdout.read())
    return data


def check(mac):
    file_content = open(
        current_path, "r", encoding="utf-8", errors="ignore"
    ).readlines()

    for line in file_content:
        (device_name, mac_address) = line.strip().split(",")
        mac_address = mac_address.replace(" ", "")

        if mac_address.lower() == mac.lower():
            print("-", mac_address, ",", Fore.GREEN + device_name + Fore.RESET)
            return True


def main():
    while True:
        user_input = input("Check mac address: ")
        if not user_input:
            continue

        if user_input in "eE":
            sys.exit()
        if user_input in "clipboard":
            clipboard()

        for address in user_input.strip().replace(" ", "").split(","):
            if not check(address):
                print("-", Fore.RED + address + Fore.RESET)


def clipboard():
    clip = get_clipboard_data()

    reCompiler = compile(u"(?:[0-9a-fA-F]:?){12}")
    reResults = findall(reCompiler, clip)

    if reResults:
        for i in reResults:
            if ":" not in i:
                continue

            if not check(i):
                print("-", Fore.RED + i + Fore.RESET)


try:
    current_path = path.dirname(path.realpath(__file__)) + "/maclist.txt"
    if not path.exists(current_path):
        open(current_path, "w").close()
    clipboard()
    main()
except KeyboardInterrupt:

    print()
    sys.exit()
