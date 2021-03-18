## Scrap Latest Torrents

This script downloads the torrents in our Torrent client from the website https://rarbg.to/ from an entered label.

### Requirements

1.  You must have a torrent client, for example: uTorrent, BitTorrent, etc
a.  You can download **uTorrent** from here: www.utorrent.com
b.  You can download **BitTorrent** from here: www.bittorrent.com

### Setup

1.  Create a Virtual Environment.
a.  `$ git clone <Project> # Cloning project repository`
b.  `$ cd <Project> # Enter to project directory`
c.  `$ python3 -m venv my_venv # If not created, creating virtualenv`
&nbsp;&nbsp;&nbsp;&nbsp; - If you use Windows: `my_env/Script/activate # Activating virtualenv`
&nbsp;&nbsp;&nbsp;&nbsp; - If you use Linux or Mac: `$ source ./my_env/bin/activate # Activating virtualenv`
**More Info**: [Virtual Environments and Packages](https://docs.python.org/3/tutorial/venv.html)
2.  Install the requirements by using  `pip3 install -r requirements.txt`

### Running a File

1.  Run the Script  `python scrap_latest_torrents.py`
2.  Enter the label to search, example: Mr Robot.
3.  The number of Torrents found will be displayed, you must confirm the download

![How to use the script](https://i.ibb.co/PD3sPLf/Scrap-Latest-Torrents.png)

## Author(s)

**_ Made By [Diego Caraballo](https://github.com/DiegoCaraballo) _**