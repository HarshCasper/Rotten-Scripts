#!/bin/bash

function github() {
	
	baseUrl="https://github.com"
	statusCode=$(curl -I -s -L "$baseUrl/$username" | grep -w "HTTP" | cut -d " " -f2 | tail -n 1)
	if (( statusCode == 200 )); then
		echo "$username exists on Github"
	else 
		echo "$username does not exists on Github"
	fi
}

function reddit() {
	baseUrl="https://www.reddit.com/user"
	for i in {1..5}; do
		statusCode=$(curl -I -s -L "$baseUrl/$username" \
	   -H 'upgrade-insecure-requests: 1' \
  	   -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36' \
  	   -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  	   -H 'accept-language: en-GB,en;q=0.9' \
  	   --compressed | grep -w "HTTP" | cut -d " " -f2 | tail -n 1)

	  if (( statusCode == 200 )); then
	  	echo "$username exists on Reddit"
	  	break
	  elif (( statusCode == 404 )); then
	  	echo "$username does not exists on Reddit"
	  	break
	  elif (( statusCode == 504 )); then
	  	continue
	  else
	  	echo "$username does not exists on Reddit"
	  	break
	  fi
	done
}

function devTo() {
	baseUrl="https://dev.to"
	statusCode=$(curl -I -s -L "$baseUrl/$username" | grep -w "HTTP" | cut -d " " -f2 | tail -n 1)
	if (( statusCode == 200 )); then
		echo "$username exists on DEV Community"
	else 
		echo "$username does not exists on DEV Community"
	fi
}

function huntSocialMedia() {
	github
	reddit
	devTo

}

username=$1
if [ -z $1 ]; then
	read -p "Enter Username: " username
fi

huntSocialMedia
