#! /bin/bash
#Simple Bash Script to generate Password
echo "Password Generator"
sleep 1
echo "_______________________________________________ "
echo "Enter the length of the password: "
read passlen
for i in $(seq 1);
do
        openssl rand -base64 48 | cut -c1-$passlen
done
