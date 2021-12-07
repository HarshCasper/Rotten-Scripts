#!/bin/bash

#https://drive.google.com/file/d/<fileId>/view?usp=sharing # <--- Link of the file on Gdrive to be downloaded 
if [ "$#" -lt 2 ] 
then 
    echo "Usage: ./driveDownload.sh [fileID] [fileName]"
    exit 1
fi

fileid=$1
filename=$2
curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=${fileid}" > /dev/null
curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=$(awk "/download/ {print $NF}" ./cookie)&id=${fileid}" -C - --output ${filename}
