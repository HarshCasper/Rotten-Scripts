import subprocess

print(
    "Press the key to Launch Computer Programs:\n 0 : Calculator\n 1 : Wordpad\n 2 : Notepad "
)
try:
    choice = int(input("\nEnter your Choice : "))
    applicationName = ("calc", "write", "notepad")
    subprocess.Popen("C:\\Windows\\System32\\" + str(applicationName[choice]) + ".exe")
except Exception as err:
    print(f"Error Occurred. Please try again.\n{err}")
