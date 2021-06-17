# Bookmarks Keeper

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/open-source.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-markdown.svg)](https://forthebadge.com)
[![Bash Shell](https://badges.frapsoft.com/bash/v1/bash.png?v=103)](https://github.com/ellerbrock/open-source-badges/)

Bookmarks Keeper is a simple bash script which when executed with out any argument gets all the bookmarks from all the major browsers(Google Chrome, Mozilla Firefox, Brave Browser and Chromium) installed on your system and stores all the bookmarks in a markdown file named bookmarks.md.
This script when used with a task scheduler can be used for bookmark backup. This script can also take a single argument and search for bookmarks with that particular pattern and stores them in bookmarks.md file.

## Setup Instructions

- For running the script when we are in the same directory where bookmarksKeeper.sh resides, execute the following command.

  > bash bookmarksKeeper.sh

- For the running script from anywhere regardless of the directory the current user is in, move the file **bookmarksKeeper.sh** to **_/usr/local/bin_**.

  1. To do so execute the following command:

     > sudo cp bookmarksKeeper.sh /usr/local/bin

  2. Then give execute permission to the script.

     For adding execute permission, run the following command:

     > sudo chmod +x /usr/local/bin/bookmarksKeeper.sh

  3. Now you can run the script using the follwing command:

     > bookmarksKeeper.sh

## Usage

To get all the bookmarks regardless of filtering, run the script as follows(assuming script is not located in /usr/local/bin and we are in the same directory where bookmarksKeeper.sh is located):

> bash bookmarksKeeper.sh

We can also provide an argument to the script to filter out and store only those bookmarks in the markdown file which contains that argument.

To doing so execute the following command:

> bash bookmarksKeeper.sh mozilla

## Note

To change the location where the markdown file will be stored, you can modify the **_location_** variable in the script.

## Output

![sample-output](https://imgur.com/zV7HCU8.png)

## Author(s)

**_ Made By [Ashutosh Kumar](https://github.com/Blastoise) _**
