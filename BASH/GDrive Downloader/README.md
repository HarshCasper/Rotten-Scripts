# Google Drive Downloader

* A simple BASH script to download files from Google Drive that allows resuming the downloads in case of failures.
* Uses cURL to achieve the same.

## Note: 

The script only works on google drive links that allow anyone on the internet with it to view the file and have the following format:

```
https://drive.google.com/file/d/<fileID>/view?usp=sharing
```

## Setup instructions

### Dependencies

- [cURL](https://curl.se/)

### Usage

Install the dependencies:
```bash
$ sudo apt install curl
```

Get the file's link by right clicking on it and selecting the `Get link` option. Change the permissions as shown in the image below and copy the `fileID` portion of this link.
<table>
    <tr>
        <td valign="top"><img src="https://imgur.com/uiVIR45.jpg"></td>
        <td valign="top"><img src="https://imgur.com/wpyKx8d.jpg"></td>
    </tr>
</table>

Download the file by passing the `fileID` present in the file's link (as shown above) and a `fileName` of your choice as command line arguments to the script. `fileName` is important for resuming downloads in case they fail in the middle.

```bash
$ chmod +x ./driveDownload.sh
$ ./driveDownload.sh <fileID> <fileName> 
```

In case a download fails, just rerun the above command with the same arguments and the download will resume from where it had stopped! 
No progress lost!!

## Output

### Without any failures:

![No failures](https://imgur.com/NLIFvll.jpg)

### Manually stopping and resuming the download:

![Resuming Failed Download](https://imgur.com/BMu0nKu.jpg)

## Author

[Dhruval PB](https://github.com/Dhruval360)
