# Twitter_Followers_Overlap

**Twitter_Followers_Overlap** a script to list the followers that are common between two twitter users.
- It uses Twitter API to fetch followers of any user *(provided as input)*.
- Then compares them to give names of people that are common between both the users.

## Setup instructions

- Get your [Twitter developer account](https://developer.twitter.com/en) and follow the steps there to generate your **bearer key**
- In a file named `apiTokens.js` in the Twitter_Followers_Overlap folder, enter your bearer key : ![File content](https://i.imgur.com/qGWVd7h.png)
- Open terminal and do the following : 
- `cd Rotten-Scripts\JavaScript\Twitter_Followers_Overlap`
- Run `npm install` to install all necessary dependencies
- Run `node Twitter_Followers_Overlap.js` and Voila! you are ready to go 😉

## Output

![Output Pic](https://i.imgur.com/9klb2d9.png)

## Author(s)

Hi I'm [Madhav Jha](https://github.jhamadhav.com) author of this script.

## Disclaimer

- **DO NOT forget to get your bearer key from your [Twitter developer account](https://developer.twitter.com/en) and ALWAYS keep it a SECRET!!!**
- **Do not try for accounts with followers count more than few thousands, even though the script works you will exhaust your twitter API limit before the process ends.**
