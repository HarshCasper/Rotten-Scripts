"""
This script downloads the torrents in our Torrent client from the
website https://rarbg.to/ from an entered label.
"""

import subprocess
import os
import sys
import rarbgapi


def main():
    """
    Principal function
    """
    count = 0

    # Label to search
    label = input("Enter a label: ")

    # Search Torrents
    torrents = search_torrents(label)

    # If no torrents were found
    if len(torrents) == 0:
        another_search = input(
            str(len(torrents))
            + " torrents found, do you want to do another search? y/n :"
        )
        if another_search.upper() == "Y" or another_search.upper() == "YES":
            main()
    else:
        # Option User
        option = input(
            str(len(torrents)) + " torrents found Do you want to download them? y/n :"
        )

        if option.upper() == "Y" or option.upper() == "YES":
            print("Downloading torrents... please wait")
            for torrent in torrents:
                open_file(torrent.download)
                count += 1
                print(str(count) + " - " + str(torrent))
        else:
            exit_option = input("Do you want to do another search? y/n :")
            if exit_option.upper() == "Y" or exit_option.upper() == "YES":
                main()

    print("Exit")


def open_file(filename):
    """
    Function that opens the torrent file according to the operating system
    """
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])


def search_torrents(label):
    """
    Function that searches for torrents from the RARBG API
    """

    print("Searching torrents... please wait")

    client = rarbgapi.RarbgAPI()
    torrents = client.search(search_string=label, limit=100)

    return torrents


if __name__ == "__main__":
    main()
