#!/bin/bash

# This script shows your public ip address

# if [ "$1" == "-help" ] || [ "$1" == "--help" ] || [ "$1" == "-h" ]; then
#     echo "This script shows you public IP address"
#     exit 0;
# fi

# function help_menu() {
#     echo "help menu.."
#     # if [ "$1" == "-help" ] || [ "$1" == "--help" ] || [ "$1" == "-h" ]; then
#     #     echo "This script shows you public IP address"
#     #     exit 0;
#     # fi
#     echo "Usage ./$0  : prints your public IPaddress \
#                 ./$0 <website url> : prints website ipaddress"
#     exit 0
# }

CLI_ARGS=$#
WEBSITE=$1

function get_public_ip_addr() {
  result=$(wget https://ipinfo.io/ip -qO -)
  echo "Your public IP is: $result"
}

function get_website_ip_addr() {
  nslookup $WEBSITE | grep Address: > temp.txt

  filename='temp.txt'
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
  if [ $CLI_ARGS -eq 0 ]; then
    get_public_ip_addr
  else
    get_website_ip_addr $WEBSITE
  fi
}

function main() {
  get_ipaddr
}


# start of the main program..
main
