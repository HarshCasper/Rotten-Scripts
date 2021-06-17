#!/bin/bash

# commands used by this script
DEPS=("grep" \
      "sed" \
      "curl" \
      "perl" \
      "youtube-dl")

# website to scrape listings from
DOMAIN="https://www.khanacademy.org"

# check for the existence of dependencies
check_commands() {
    for COMMAND in "$@"; do
        if ! command -v "$COMMAND" > /dev/null 2>&1; then
            echo "command not found: $COMMAND"
            exit 1
        fi
    done
}

# show a general-purpose menu with numbered entries
menu_entry() {
    for i in $(seq 1 $#); do
        # parse html escapes, such as '&quot;' and '&amp;' as '"' and '&' respectively
        echo "  [$i]" "$(echo "${!i}" | perl -MHTML::Entities -pe 'decode_entities($_);')"
    done

    read -p "Enter number to select: " SELECTION
    SELECTION=$(( $SELECTION - 1 ))
}

# apply regex patterns to extract the list of topics
extract_topics() {
    local IFS=$'\n'

    REGEX_MATCH=$(curl -s "$DOMAIN" | grep -Po '>Courses</h3><ul>.*?</ul>' | grep -Po 'href="/[^/]*?"[^>]*?>[^<]+?<')
    TOPIC_TITLES=( $(echo "$REGEX_MATCH" | grep -Po '>[^<]+?<' | sed 's/[><]//g') )
    TOPICS=( $(echo "$REGEX_MATCH" | grep -Po 'href=".*?"' | sed 's/href="\///;s/"//') )
}

# apply regex patterns to extract the list of subtopics
extract_subtopics() {
    local IFS=$'\n'
    TOPIC="$1"

    REGEX_MATCH=$(curl -s "$DOMAIN/$TOPIC" | grep -Po 'href="/'"$TOPIC"'/[^/"]*?">[^<]+?<')
    SUBTOPIC_TITLES=( $(echo "$REGEX_MATCH" | grep -Po '>[^<]+?<' | sed 's/[><]//g') )
    SUBTOPICS=( $(echo "$REGEX_MATCH" | grep -Po 'href=".*?"' | sed 's/href="\///;s/"//') )
}

# apply regex patterns to extract the list of chapters
extract_chapters() {
    local IFS=$'\n'
    SUBTOPIC="$1"

    REGEX_MATCH=$(curl -s "$DOMAIN/$SUBTOPIC" | grep -Po 'href="/'"$SUBTOPIC"'/[^/#]*?"[^>]*?><h3.*?</h3>')
    CHAPTER_TITLES=( $(echo "$REGEX_MATCH" | grep -Po '>[^<]+?<' | sed 's/[><]//g') )
    CHAPTERS=( $(echo "$REGEX_MATCH" | grep -Po 'href=".*?"' | sed 's/href="\///;s/"//') )
}

# invoke youtube-dl to list the videos under the discovered playlist
extract_videos() {
    local IFS=$'\n'
    CHAPTER="$1"

    VIDEO_TITLES=( $(youtube-dl --flat-playlist --get-title "$DOMAIN/$CHAPTER") )
    VIDEOS=( $(youtube-dl --get-id "$DOMAIN/$CHAPTER") )
}

check_commands "${DEPS[@]}"

echo -e "\nFetching course topics..."
extract_topics
echo -e "Select topic:"
menu_entry "${TOPIC_TITLES[@]}"

echo -e "\nFetching subtopics under \"${TOPIC_TITLES[$SELECTION]}\"..."
extract_subtopics "${TOPICS[$SELECTION]}"
echo -e "Select subtopic:"
menu_entry "${SUBTOPIC_TITLES[@]}"

echo -e "\nFetching chapters under \"${SUBTOPIC_TITLES[$SELECTION]}\"..."
extract_chapters "${SUBTOPICS[$SELECTION]}"
echo -e "Select chapter:"
menu_entry "${CHAPTER_TITLES[@]}"

echo -e "\nFetching videos under \"${CHAPTER_TITLES[$SELECTION]}\"..."
extract_videos "${CHAPTERS[$SELECTION]}"
echo -e "Select video:"

# some chapters have only text materials and no videos
if [[ "${#VIDEO_TITLES[@]}" = "0" ]]; then
    echo -e "No videos found!"
else
    menu_entry "${VIDEO_TITLES[@]}"

    VIDEO_URL="https://youtube.com/watch?v=${VIDEOS[$SELECTION]}"
    echo -e "\nURL of selected video: $VIDEO_URL"
    read -p "Download video (y/n)? " SAVE
    if [[ "$SAVE" = 'y' || "$SAVE" = 'Y' ]]; then
        youtube-dl "$VIDEO_URL"
    else
        echo -e "Aborting..."
    fi
fi
