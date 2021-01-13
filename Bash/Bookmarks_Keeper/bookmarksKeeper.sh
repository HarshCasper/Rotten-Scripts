#!/bin/bash

# Google Chrome
function chromeBookmarks() {

	# Check whether google-chrome/Default folder exists in ~/.config folder or not
	if [ -d "${HOME}/.config/google-chrome" -a -d "${HOME}/.config/google-chrome/Default" ]; then
		file_path=$(find "${HOME}/.config/google-chrome/Default" -iname "Bookmarks")

		# if the file does not exists then there are no bookmarks
		if [ -z "$file_path" ]; then
			echo "Currently there are no bookmarks for Google Chrome" >&2
			return
		else
			echo -e "## Google Chrome\n" >>  "${location}/bookmarks.md"
			echo "---" >> "${location}/bookmarks.md"
			contents=$(cat "${file_path}")
			contents=$(echo "$contents" | grep -w "\"url\":" | tr -s " " " " | cut -d " " -f3 | grep -i "$word")
			echo "$contents" | awk '{print "-",$0}' >> "${location}/bookmarks.md"
			echo -e "\n" >> "${location}/bookmarks.md"
		fi
	else
		echo "Google Chrome not found for ${USER} user" >&2
	fi
}	

# Mozilla Firefox
function firefoxBookmarks() {

	# Check whether .mozilla/firefox folder exists or not
	if [ -d "${HOME}/.mozilla" -a -d "${HOME}/.mozilla/firefox" ]; then
		file_path=$(find "${HOME}/.mozilla/firefox/" -iname "places.sqlite")

		# if the file does not exists then there are no bookmarks
		if [ -z "$file_path" ]; then
			echo "Currently there are no bookmarks for Mozilla Firefox" >&2
			return
		else
			echo -e "## Mozilla Firefox\n" >>  "${location}/bookmarks.md"
			echo "---" >> "${location}/bookmarks.md"
			query="select p.url from moz_places as p, moz_bookmarks as b where p.id = b.fk;"
			bk=$(sqlite3 "${file_path}" "${query}" | grep -i "$word")
			echo "$bk" | awk '{print "-",$0}' >> "${location}/bookmarks.md"
			echo -e "\n" >> "${location}/bookmarks.md"
		fi
	else
		echo "Mozilla Firefox not found for ${USER} user" >&2
	fi
}

# Brave Browser
function braveBookmarks() {

	# Check whether BraveSoftware/Brave-Browser folder exists in ~/.config folder or not
	if [ -d "${HOME}/.config/BraveSoftware" -a -d "${HOME}/.config/BraveSoftware/Brave-Browser" ]; then
		file_path=$(find "${HOME}/.config/BraveSoftware/Brave-Browser" -iname "Bookmarks")

		# if the file does not exists then there are no bookmarks
		if [ -z "$file_path" ]; then
			echo "Currently there are no bookmarks for Brave Browser" >&2
			return
		else
			echo -e "## Brave Browser\n" >>  "${location}/bookmarks.md"
			echo "---" >> "${location}/bookmarks.md"
			contents=$(cat "${file_path}")
			contents=$(echo "$contents" | grep -w "\"url\":" | tr -s " " " " | cut -d " " -f3|grep -i "$word")
			echo "$contents" | awk '{print "-",$0}' >> "${location}/bookmarks.md"
			echo -e "\n" >> "${location}/bookmarks.md"
		fi
	else
		echo "Brave Browser not found for ${USER} user" >&2
	fi
}	

# Chromium
function chromiumBookmarks() {


	# Check whether chromium/Default folder exists in ~/.config folder or not
	if [ -d "${HOME}/.config/chromium" -a -d "${HOME}/.config/chromium/Default" ]; then
		file_path=$(find "${HOME}/.config/chromium/Default" -iname "Bookmarks")

		# if the file does not exists then there are no bookmarks
		if [ -z "$file_path" ]; then
			echo "Currently there are no bookmarks for Chromium" >&2
			return
		else
			echo -e "## Chromium\n" >>  "${location}/bookmarks.md"
			echo "---" >> "${location}/bookmarks.md"
			contents=$(cat "${file_path}")
			contents=$(echo "$contents" | grep -w "\"url\":" | tr -s " " " " | cut -d " " -f3 | grep -i "$word")
			echo "$contents" | awk '{print "-",$0}' >> "${location}/bookmarks.md"
			echo -e "\n" >> "${location}/bookmarks.md"
		fi
	else
		echo "Chromium not found for ${USER} user" >&2
	fi
}


# Location where the output file will be stored
location=${HOME}
# Variable to be searched in the url's
word=$1

# Delete bookmarks.md if it exists
[ -f "${location}/bookmarks.md" ] && rm "${location}/bookmarks.md"

# Executing functions for various browsers
chromeBookmarks
firefoxBookmarks
braveBookmarks
chromiumBookmarks

# If bookmarks.md exists then output it's path
[ -f "${location}/bookmarks.md" ] && printf %"$COLUMNS"s | tr " " "-" && echo "bookmarks.md created at ${location}"
