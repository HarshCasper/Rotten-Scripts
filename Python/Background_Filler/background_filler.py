from os import path
import time
import random
import sys

def main():
    filler = ""
    type_of_filler = random.choice(["poem.txt", "coding.txt"])
    file_path = path.join(path.dirname(__file__), type_of_filler)
    with open(file_path, "r") as f:
        filler = f.readlines()
    while True:
        fill_background(filler)


def fill_background(filler: list) -> None:
    """
    This function keeps printing a poem on terminal until
    you type 'Ctrl + c'. 'speed_list' is used to make printing
    like human-typing.
    """
    speed_list = [0.04, 0.1, 0.3]
    for line in filler:
        for c in line:
            time.sleep(random.choice(speed_list))
            print(c, end="", flush=True)
        print("\n")

if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n" + "Bye.")
        sys.exit()
