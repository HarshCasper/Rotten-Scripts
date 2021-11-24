# Google Drive Downloader
Frustrated of failing Google Drive Downloads?
Have to restart downloading that darn file again and again?
Well, you are in luck!!
This script gives you peace of mind while downloading files from Google Drive. Downloads can be resumed later if your internet connection is lost!! No progress lost!!

## Note: 
The script is tested only on sharable google drive links of the following format:

```
https://drive.google.com/file/d/<fileID>/view?usp=sharing
```

## Dependencies
- [cURL](https://curl.se/)

## Usage
Install the dependencies:
```bash
$ sudo apt install curl
```

Get the file's link by right clicking on it and selecting the `Get link` option. Copy the `fileID` portion of this link (again, this link should be of the format shown above).
<table>
    <tr>
        <td valign="top"><img src="./Images/1.png"></td>
        <td valign="top"><img src="./Images/2.png"></td>
    </tr>
</table>

Download the file by passing the **fileID** present in the file's link (as shown above) and a **fileName** of your choice as command line arguments to the script. The **fileName** is important for resuming downloads in case they fail in the middle.

```bash
$ chmod +x ./driveDownload.sh
$ ./driveDownload.sh <fileID> <fileName> 
```

In case a download fails, just rerun the above command with the same arguments and the download will resume from where it had stopped! No progress lost!!

### Author: [Dhruval PB](https://github.com/Dhruval360)