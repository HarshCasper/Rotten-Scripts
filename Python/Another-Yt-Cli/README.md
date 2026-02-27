# Yet Another yt-cli

- **What can it do as of now ?**
> It can query the input entered by user on youtube and get the first matching result, and play it in the video player.

- **Things to improve:**
> - Let the user choose the video by giving them the first 10 or so search results.
> - Allow users to set the resolution as per their preference.

---
## Demo:
<img src="https://imgur.com/3gdz7KA.gif" width=100%>

### **Requirements**:
The following packages need to be installed:
```
beautifulsoup4==4.10.0
certifi==2021.10.8
charset-normalizer==2.0.12
idna==3.3
lxml==4.8.0
requests==2.27.1
soupsieve==2.3.1
urllib3==1.26.8
youtube-dl==2021.4.26
```
To install the above packages, change directory to the project folder
```shell
cd another-yt-cli
```
Now install the packages by running,
```shell
pip install -r requirements.txt
```
And. now to run the program, type
```shell
python main.py
```
> **Note: You will also require the mpv player to be in your path to play the videos

Repo link: https://github.com/Skyhero-admin/another-yt-cli

Contributers: [Skyhero-admin](https://github.com/Skyhero-admin)