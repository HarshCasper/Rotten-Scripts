# Khan Academy Downloader

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/open-source.svg)](https://forthebadge.com)
[![Bash Shell](https://badges.frapsoft.com/bash/v1/bash.png?v=103)](https://github.com/ellerbrock/open-source-badges/)

Khan Academy Downloader is a bash script which fetches all the course names from the [Khan Academy website](https://www.khanacademy.org/) and displays a menu to select those from.
The user can select an entry from that menu to download the corresponding video for offline watching.

## Setup and Usage Instructions

- Make sure you have got curl, perl, perl-HTML-parser, youtube-dl and coreutils (includes grep and sed) installed on your machine.
  - For Debian/Ubuntu:
    > sudo apt install perl-HTML-parser youtube-dl coreutils
  
  - For RHEL/Fedora:
    > sudo dnf install perl coreutils
    
    > pip3 install youtube-dl
    
    > wget http://rpmfind.net/linux/RPM/mageia/cauldron/aarch64/media/core/release/perl-HTML-Parser-3.760.0-1.mga9.aarch64.html
    
    > sudo dnf install http://rpmfind.net/linux/mageia/distrib/cauldron/aarch64/media/core/release/perl-HTML-Parser-3.760.0-1.mga9.aarch64.rpm
    
    > sudo dnf install perl-HTML-Parser
    
  - For Arch Linux:
    > sudo pacman -S perl-HTML-parser youtube-dl coreutils

- For running the script as a local user, just navigate to the directory where khanacademy-dl.sh resides, and execute the following command:

  > bash khanacademy-dl.sh

- For running the script from anywhere, regardless of the current directory, copy the file **khanacademy-dl.sh** to **_/usr/local/bin/_**.

  1. To do so execute the following command:

     > sudo cp khanacademy-dl.sh /usr/local/bin

  2. Then set the executable bit on the script:

     > sudo chmod +x /usr/local/bin/khanacademy-dl.sh

  3. You can now run the script using the following command:

     > khanacademy-dl.sh

## Output

![sample-output](https://imgur.com/zV7HCU8.png)

## Author(s)

[Prateek Ganguli](https://github.com/pganguli)
