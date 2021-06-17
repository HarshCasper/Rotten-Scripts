#!/bin/bash

# Variable to be modified according to internet speed
# If your internet speed is fast a value of 2 or 3 will be great
sleep_time=5

# Varible where Chrome Driver is located
driver_location="${HOME}"

# Complete path of the markdown file to be created
location_of_file="${HOME}/twitterBookmarks.md"

function login() {

	# Open Twitter login page
	curl -s -d '{"url":"https://twitter.com/login"}' ${baseUrl}/${sessionId}/url > /dev/null
	sleep "$sleep_time"

	# Element ID for username
	usernameID=$(curl -s ${baseUrl}/${sessionId}/element -d '{"using":"name","value":"session[username_or_email]"}' | jq '.value.ELEMENT' | cut -d '"' -f2)

	# Type out the username in the username field
	curl -s ${baseUrl}/${sessionId}/element/${usernameID}/value -d "{\"value\":[\"$username\"]}" > /dev/null

	# Element ID for password
	passwordID=$(curl -s ${baseUrl}/${sessionId}/element -d '{"using":"name","value":"session[password]"}' | jq '.value.ELEMENT' | cut -d '"' -f2)
	
	# Type out the password in the password field
	curl -s ${baseUrl}/${sessionId}/element/${passwordID}/value -d "{\"value\":[\"$password\"]}" > /dev/null

	# Element ID for button
	buttonID=$(curl -s ${baseUrl}/${sessionId}/element -d '{"using":"xpath","value":"//div[@data-testid=\"LoginForm_Login_Button\"]"}' | jq '.value.ELEMENT' | cut -d '"' -f2)

	# Click the button
	curl -s -XPOST ${baseUrl}/${sessionId}/element/${buttonID}/click > /dev/null

	sleep "$sleep_time"
}

function getAllUrls() {


	# Go to the bookmarks URL
	curl -s -d '{"url":"https://twitter.com/i/bookmarks"}' ${baseUrl}/${sessionId}/url > /dev/null

	sleep "$sleep_time"

	# Associative Array that stores URL as keys
	declare -A tweets

	# Height to be scrolled
	height=1000

	# Variable to check after each iteration
	scrolling="true"

	# Get the y-position of scroll bar
	prev_pos=$(curl -s -d '{"script":"return window.pageYOffset;","args":[]}' ${baseUrl}/${sessionId}/execute | jq '.value')

	while [ "$scrolling" = "true" ]; do

		# Get the id's of the anchor tag of the tweets
		arr=($(curl -s ${baseUrl}/${sessionId}/elements -d '{"using":"xpath","value":"//a[./time]"}' | jq '.value[] | .ELEMENT' | cut -d '"' -f2)) 

		# Loop for getting url for those tweets which are not repetative
		for i in ${arr[@]}; do 

			# Getting the URL
			temp_url=$(curl -s ${baseUrl}/${sessionId}/element/${i}/attribute/href | jq .value | cut -d '"' -f2)

			# Saving the URL if it doesn't exists
			if [ -z "${tweets[${temp_url}]}" ]; then
				tweets["$temp_url"]=1
			else
				continue
			fi

		done 

		# Variable to try scrolling
		scroll_attempt=0

		while true; do

			# For scrolling the page
			curl -s -d "{\"script\":\"window.scrollTo(0,$height);\",\"args\":[]}" ${baseUrl}/${sessionId}/execute > /dev/null
			sleep "$sleep_time"

			# Getting the current y-position of scroll bar
			current=$(curl -s -d '{"script":"return window.pageYOffset;","args":[]}' ${baseUrl}/${sessionId}/execute | jq '.value')

			# If the scrolling didn't happen then try again
			if (( $(echo "$current == $prev_pos" | bc -l) )); then
				((scroll_attempt=scroll_attempt+1))

				# We reached the end of tweets
				if [ "$scroll_attempt" -ge 5 ] ;then
					scrolling="false"
					break
				else
					sleep "$sleep_time"
				fi
			else
				prev_pos=$current
				((height=height+1000))
				break
			fi

		done
		
	done

	# Adding URl's to the markdown file
	touch "$location_of_file" && echo -e "# Twitter Bookmarks\n" >> "$location_of_file"

	for i in "${!tweets[@]}"; do
		echo -e "- $i" >> "$location_of_file"
	done

	echo "${location_of_file} file created and saved"

}


username=$1
password=$2

if [ -z "$username" ]; then
	read -p "Enter Username: " username
	read -s -p "Enter password: " password
elif [ -z "$password" ]; then
	read -s -p "Enter password: " password
fi


# Location where web driver is located
cd "$driver_location"

# Running the web driver in the background
./chromedriver &

# Create a session and store the sessionId
baseUrl="http://localhost:9515/session"
sessionId=$(curl -s -d '{"desiredCapabilities":{"browserName":"chrome","goog:chromeOptions":{"args":["headless"]}}}' ${baseUrl} | jq '.sessionId' | cut -d '"' -f2)

# Function to login into Twitter
login

# Function to get Tweets and saving them in Markdown.md file
getAllUrls
