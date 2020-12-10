#!/bin/bash
# file: /usr/local/bin/Ports_Scan
PS3='Please enter your choice: '
options=$(lsof -PiTCP -sTCP:LISTEN | awk '{print $9}' | sed -n '1!p')
RED='\033[0;31m'
# No Color
NC='\033[0m'
select port in $options
do
  echo "Selected character: $port"
  echo "Selected number: $REPLY"
  var2=$(echo $port | cut -f2 -d:)
  echo -e "killing ${RED}port $var2 ${NC}!"
  # shellcheck disable=SC2046
  # shellcheck disable=SC2005
  echo $(lsof -ti tcp:"$var2" | xargs kill)
  exit 0
done