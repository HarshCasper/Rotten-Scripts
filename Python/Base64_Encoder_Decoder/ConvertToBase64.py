# This script is capable of converting some special/secret text
# into 64 BASE Encoded String

# importing base64

def ConvertToBase64():
	import base64

	string = input("Enter string to encode:")

	# encoding the string to base64
	string = base64.b64encode(string.encode('utf-8'))
	print(string)

	# decoding the string to base64
	print("Want to decode(Y/N):")
	choice = input()
	if(choice == 'y' or choice == 'Y'):
	    print("Decoded String:")

	    #decoding the given string
	    string = base64.b64decode(string).decode('utf-8')
	    print(string)
	else:
	    print("String Encoded")
ConvertToBase64()