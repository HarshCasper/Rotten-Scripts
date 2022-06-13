#!/bin/bash

# This script shows your public ip address

CLI_ARGS="$#"
WEBSITE="$1"

function get_public_ip_addr() {
  result=$(wget https://ipinfo.io/ip -qO -)
  echo "Your public IP is: $result"
}

function get_website_ip_addr() {
  nslookup "$WEBSITE" | grep Address: > temp.txt

  filename="temp.txt"

  n=1
  while read line; do
  if [ "$n" == 2 ] ; then
      echo "The IP address of [ $1 ] is: ${line:9}"
  fi
  n=$((n+1))
  done < $filename

  rm temp.txt
}


# function to check for the ipaddress of your system as well as for websites
function get_ipaddr() {
  if [ "$CLI_ARGS" -eq 0 ]; then
    get_public_ip_addr
  else
    get_website_ip_addr "$WEBSITE"
  fi
}


function main() {
  get_ipaddr
}


# start of the main program..
main
