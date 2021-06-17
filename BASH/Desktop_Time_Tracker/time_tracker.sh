#!/bin/bash

draw_pie_chart() {
declare -n apps_names_array=$1
declare -n win_app_array=$2

# This array obtain the time information only from the win array to use it to draw the pie chart
time_elapsed_array=()
for((i=2;i<${#win_app_array[@]};i+=3)); do
	time_elapsed_array+=("${win_app_array[i]}")
done

# To be plotted
echo -e "To be plotted ${apps_names_array[@]}\n ${time_elapsed_array[@]}\n"

}

# Update frequency in seconds
update_frequency=1
# Pie chart update frequency in seconds
pie_chart_update_frequency=1
# Array that stores all apps names
app_array=()
# Array that stores corresponding information to those apps in applist
# This array holds (app_name, executed_path, time_elapsed)
# Accessing in this array will be in multiple of 3, because each app holds 3 entities in the array
# e.g. (app1_name, app1_path, app1_time, app2_name, app2_path, app2_time)
win_array=()
# Get the current working directoy to save the pie chart
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Main Loop
while true
do
	# Sleep for the update frequency
	sleep $update_frequency
	# Get the current opened window process id
	frpid=$(xdotool getactivewindow getwindowpid)
	# Get the current opened window name
	frname=$(xdotool getactivewindow getwindowname)
	# Obtain the app name using ps terminal command
	app="$(ps -p $frpid -o comm=)"	# echo $app
	# adding the app to the app list
	if [[ " ${app_array[*]} " != *"$app"* ]]; then
		echo "New App is opened, tracking it..."
		app_array+=($app)
	fi

	checklist=()
	for ((i=1;i< ${#win_array[@]} ;i+=3)); 	do
		checklist+=("${win_array[i]}")
	done

	if [[ "${checklist[@]}" == *"$frname"* ]]; then
		# The app has already a history of time elapsed, we have to increment the time only

		# Getting the app index
		for ((k=0; k<${#checklist[@]}; k++)); do
			if [[ "${checklist[$k]}" == *"$frname"* ]]; then
				# Incrementing, the 3*k+2 term: 3*k because each app holds 3 entries
				#				+2  because we're accessing the time element regarding this app
				win_array[$(("3*$k+2"))]="$(("${win_array[$((3*k+2))]}" + "$update_frequency"))"
			fi
		done
	else
		temp_arr=("$app" "$frname" "$update_frequency")
		win_array+=("${temp_arr[@]}")
	fi
	draw_pie_chart  app_array win_array
done
