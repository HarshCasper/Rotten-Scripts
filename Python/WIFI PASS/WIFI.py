#import necessary files

import subprocess 

#Open file that will store the wifi passwords in write mode

file_object = open('message.txt', 'w')

#via subprocess execute the netsh command on commandline
#store the output in list

a = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
a = [i.split(":")[1][1:-1] for i in a if "All User Profile" in i]

#iterate through each wifi key and their pass and store it in the file

for i in a:
	results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
	results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
	
	try:
		#print("{:<30}|  {:<}".format(i, results[0]))		 #to debug
		
		#write the content in the file

		file_object.write(str(i) + " " + str(results[0]))
		
	except IndexError:
		print("{:<30}|  {:<}".format(i, ""))

file_object.close()