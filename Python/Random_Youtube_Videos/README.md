
# Random Yotutbe Videos

This Python Script fetches random youtube videos on every iteration and opens a random Youtube Video.

## Setup instructions

#### Create a Google Account / Use an Existing Google Account and Head to : https://console.developers.google.com/ 

#### Click on Select a Project > NEW PROJECT

<img src="https://i.imgur.com/w94hs03.png" title="source: imgur.com" alt="Step2a"/>
<img src="https://i.imgur.com/hDSzM1c.png" title="source: imgur.com" alt="Step2b"/>

#### Enter a Project name and click on Create

<img src="https://i.imgur.com/aqJ8gw6.png" title="source: imgur.com" alt="Step3"/>

#### Select the created project in Select a Project

<img src="https://i.imgur.com/i0N6zMW.png" title="source: imgur.com" alt="Step4"/>

#### Head to Library section

<img src="https://i.imgur.com/a6SRux3.png" title="source: imgur.com" alt="Step5"/>

#### Search for YouTube Data API v3 and enable it

<img src="https://i.imgur.com/vp1KE6Q.png" title="source: imgur.com" alt="Step6"/>

#### Click on Create Credentials

<img src="https://i.imgur.com/dOxtnzc.png" title="source: imgur.com" alt="Step7"/>

#### Click on API KEY and note your APIKEY (You will require it for searching the video)

<img src="https://i.imgur.com/FLQY0fG.png" title="source: imgur.com" alt="Step8"/>

### Once Done...

#### Open command prompt in the folder and run to install requirements:

```bash
pip install -r requirement.txt 
```

#### Rename the .env_sample file to .env and enter your API Key in place YOUR_API_KEY_HERE 

#### Run the Program using (Enter the generated key from [Steps](#steps)):

```bash
py randomyt.py
```

## Detailed explanation of script, if needed

The script uses YouTube Data API V3 Library to fetch video from youtube and a random string is given in the search query

## Output

After entering correct API a random YouTube Video will start playing

<img src="https://i.imgur.com/jTg9NeQ.png" title="source: imgur.com" alt="Step8"/>

## Author(s)

Nimish Samant - [realhunter7869](https://github.com/realhunter7869)
