# Empty Subtitles

We watch a lot of videos with subtitles. Sometimes, these videos will not have subtitles in them. Wouldn't it be nice if there was something to indicate that there are no subtitles?

That's where `emptysubs.sh` comes in handy.

## Setup Instructions

- The recommended way is to add a permanent alias to this script file in your Linux distro.
- To know how to add permanent aliases, you can refer to this [link](https://www.tecmint.com/create-alias-in-linux/).

## Output

#### *Executing the command*

After adding a permanent alias, this command has been executed to get the following output.

- The `VideosDirectory` had `mp4` files. So, the `-c` (container) argument is `mp4`.
- After the command is executed, a folder will be created with the subtitle files inside of it.

![Command Execution](https://imgur.com/oEqw8Ry.png)

#### *Checking if the files are created*

Let's check if the files have been created:

1. Using the Command Line Interface.
2. Using the Graphical Interface.

![Checking](https://imgur.com/5kBRVpQ.png)

## Author

[Kamal Sharma](https://github.com/KamalDGRT)

## Disclaimer

- Eventhough the file name is `emptysubs.sh`, it does not create empty subtiles. 
- The script creates a subtile with the text `No Subtitles Available!!!` which will be displayed for a duration of 10 seconds.
