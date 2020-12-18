#!/bin/sh
read -p 'File ID: ' file_id
read -p 'File Name with extension: ' file_name

wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate https://docs.google.com/uc\?export=download\&id=$file_id -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=$file_id" -O $file_name && rm -rf /tmp/cookies.txt
