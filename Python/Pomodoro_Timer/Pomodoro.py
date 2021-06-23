import time

# path of host file in windows
host_path = r"C:\Windows\System32\drivers\etc\hosts"

# URL of websites to block
with open("block_urls.txt", "r") as url_file:
    block_list = [url.strip() for url in url_file]

# redirecting above URLs to this localhost to ensure blocking
redirect = "127.0.0.1"


def block_websites():
    """
    The function will open the host file and add the block-list websites to
    the file if it is not already present and redirect it to the localhost
    for blocking
    """
    try:
        # Opening the host file in reading and writing mode
        with open(host_path, "r+") as h_file:
            content = h_file.read()

            for website in block_list:

                # Website is already blocked
                if website in content:
                    pass

                # To redirect the website to be blocked
                else:
                    h_file.write(redirect + "\t" + website + "\n")

        return 1

    except PermissionError:
        print(
            "\nTry running the cmd in admin mode and "
            "then run this code to enable this functionality!"
        )
        return 0

    except FileNotFoundError:
        print("\nThis functionality is not supported for your OS!")
        return 0


def remove_websites():
    """
    The function will unblock the block_list websites by opening the file
    and removing the changes we made before
    """
    try:
        # Opening the host file in reading and writing mode
        with open(host_path, "r+") as file:
            # making each line of file into a list
            content = file.readlines()

            # sets the file pointer at the beginning of the file
            file.seek(0)

            # Traversing through each line of the host file and
            # checking for the websites to be blocked
            for lines in content:
                if not any(website in lines for website in block_list):
                    file.write(lines)

            # Truncating the file to its original size
            file.truncate()

    finally:
        pass


def pomodoro():
    """
    This function has the implementation of the user-friendly Pomodoro timer
    along with the website blocking functionality.
    """
    print("\n------------------ POMODORO TIMER ------------------\n")
    print(
        "\nPomodoro timer helps to break down your work into 25 minutes of "
        "high focus intervals separated by short breaks of 5 minutes."
    )
    print(
        "\nFor extra focus, would you like to enable website blocker? "
        "\n**Selecting this option will block all of the popular "
        "social media sites throughout the 25 min duration**"
    )
    enable = input("\nPress (y) to enable and any other key to skip: ")

    cycle = 0

    while 1:
        # Feature to block social media websites
        if enable == "y":
            if block_websites():
                pass
            else:
                enable = ""

        input("\nPress any key to start the timer: ")
        cycle += 1

        # Setting a 25 minute timer
        t = 1 * 60

        # To display the time left on the screen
        while t:
            minute_count = t // 60
            second_count = t % 60
            timer = "{:02d}:{:02d}".format(minute_count, second_count)
            print(f"Time left: {timer}", end="\r")
            time.sleep(1)
            t -= 1

        # A sound to let user know the timer is over
        for i in range(2):
            for _ in range(4):
                time.sleep(0.5)
                print("\a")
            time.sleep(3)

        print("\nPOMODORO FINISHED!")
        print("Break Time!! Give yourself a 5 min break!")
        input("\nPress any key to start the break timer: ")

        # Removing the blocked websites for the break
        if enable == "y":
            remove_websites()

        t = 1 * 60
        # To display the break time left
        while t:
            minute_count = t // 60
            second_count = t % 60
            timer = "{:02d}:{:02d}".format(minute_count, second_count)
            print(f"Time left: {timer}", end="\r")
            time.sleep(1)
            t -= 1

        # A sound to let user know the timer is over
        for i in range(3):
            for _ in range(4):
                time.sleep(0.5)
                print("\a")
            time.sleep(3)

        ans = input(
            "\nWould you like to start a new Pomodoro? \n"
            "Press (y) to continue or any other key to exit: "
        ).lower()

        if ans != "y":
            return cycle


num = pomodoro()
print(f"\nGreat work! You completed {num} Pomodoro cycles! \nGood going!\n")
