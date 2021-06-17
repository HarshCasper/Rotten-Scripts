# No Subtiles Matroska 

We tend to download video files. One of such container for video files is matroska or mkv. Sometimes the subtitles present in those mkv containers would be out of sync and it might be in language which we don't know. So, it would be cool to remove those subtitles and have a clean mkv file with just audio and video.

That's where `nosubsmkv.sh` comes in handy.

## Setup instructions

- The recommended way is to add a permanent alias to this script file in your Linux distro.
- To know how to add permanent aliases, you can refer to this [link](https://www.tecmint.com/create-alias-in-linux/).
- This script uses [ffmpeg](https://ffmpeg.org/download.html) and [MKVToolNix](https://www.fosshub.com/MKVToolNix.html).

## Output

#### *Executing the command*

After adding a permanent alias, this command has been executed to get the following output.

- The `VideosDirectory` had `mkv` files. 
- After the command is executed, a `nosubsmkv` folder will be created with mkv files. 

![Command Execution](https://i.imgur.com/1w4DikS.png)

#### *Track listing of the original files*

Let's see the various tracks available in the matroska files.

![Checking](https://i.imgur.com/nTk9y9r.png)

#### *Track listing of the new files*

Let's see the various tracks available in the new matroska files.

![Checking](https://i.imgur.com/2weAkRa.png)

## Author

[Kamal Sharma](https://github.com/KamalDGRT)
