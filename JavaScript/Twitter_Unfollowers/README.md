# Twitter_Unfollowers

**Twitter_Unfollowers** is a script to track people that recently unfollowed you on Twitter.
- It uses Twitter API to fetch followers of any user *(provided as input)*.
- Then stores it into a `json` file. 
- When compared again it gives name and number of people that unfollowed.
- *(Additionally) :* After multiple queries it provides search/query history in tabular form.

## Setup instructions

- Get your [Twitter developer account](https://developer.twitter.com/en) and follow the steps there to generate your **bearer key**
- In a file named `apiTokens.js` in the Twitter_Unfollowers folder, enter your bearer key : ![File content](https://i.imgur.com/4UlveGE.png)
- Open terminal and do the following : 
- `cd Rotten-Scripts\JavaScript\Twitter_unfollowers`
- Run `npm install` to install all necessary dependencies
- Run `node Twitter_Unfollowers.js` and Voila! you are ready to go 😉

## Output

![Output Pic](https://i.imgur.com/HQ68vDj.png)

## Author(s)

Hi I'm [Madhav Jha](https://github.jhamadhav.com) author of this script.

## Disclaimer

- **DO NOT forget to get your bearer key from your [Twitter developer account](https://developer.twitter.com/en) and ALWAYS keep it a SECRET!!!**
- **Do not try for accounts with followers count more than few thousands, even though the script works you will exhaust your twitter API limit before the process ends.**
