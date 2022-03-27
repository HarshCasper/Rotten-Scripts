import requests, re, json, os, sys
from lxml import etree
from bs4 import BeautifulSoup

def get_link(name):
	query = name.split()
	r = requests.get('https://www.youtube.com/results?search_query='+ "+".join(query)).text
	# html = r.content
	# print('https://www.youtube.com/results?search_query='+ "+".join(name))
	print("Searching for "+name+"....\n")

	soup = BeautifulSoup(r, "lxml")

	script = soup.find_all("script")[33]
	# print(script)

	json_text = re.search("var ytInitialData = (.+)[,;]{1}", str(script)).group(1)
	json_data = json.loads(json_text)
	# print(json_data)

	# ME TESTING :)
	# with open("file.txt", "w", encoding='utf-8') as output:
	# 	output.write(soup.prettify())

	# with open("script.txt", "w", encoding = "utf-8") as output:
	# 	output.write(json_text)

	content = (
		json_data
		['contents']['twoColumnSearchResultsRenderer']
		['primaryContents']['sectionListRenderer']
		['contents'][0]['itemSectionRenderer']
		['contents']
	)

	for i in content:
		for key, val in i.items():
			if type(val) is dict:
				for k,v in val.items():
					# print(k)
					# print(v)
					try:
						if k == "videoId" :
							# and len(v) == 11
							# print(v)
							return "https://www.youtube.com/watch?v="+v
						# if k =="title":
							# print(v["runs"][0]["text"])
					except Exception as e:
						print("An error occured:",e)

	# dom = etree.HTML(str(soup))
	# print(dom.xpath('//*[@id="video-title"]')[0].text)
	# for i in res:
	# 	print(i)
		# print(i.a['id'])
		# if i.a['id'] == "video-title":
		# 	print(i)

# get_link()

def get_video_name():
	name = input("Enter the video name you want to play: ")
	return name

def play(link):
	if str(type(link)) == "<class 'NoneType'>":
		print("An error occured!!!")
		return

	print("Trying to play: ",link)
	os.system("mpv --ytdl-format=18 "+link)
	print()

# MAIN PROGRAM starts here
if __name__ == "__main__":
	if(len(sys.argv)>1):
		res = get_link(" ".join(sys.argv[1:]))
		play(res)
	else:
		n = get_video_name()
		res = get_link(n)
		play(res)
