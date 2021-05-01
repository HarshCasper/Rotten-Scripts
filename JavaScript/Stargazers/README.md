# Stargazers

- **Stargazers** gives list of people that have starred a repo and those who have recently un-starred.
- It uses Github API to fetch Stargazers of any repo.
- Then stores it into a `db.json` file. 
- When compared again it gives name and number of people that have recently un-starred and starred the inputted repo.

## Setup instructions

- Get your [`Github Developer Token`](https://dev.to/gr2m/github-api-authentication-personal-access-tokens-53kd) and follow the steps there to generate your **Token key**
- In a file named `tokens.js` paste the token.
- Open terminal and do the following : 
- `cd Rotten-Scripts\JavaScript\Stargazers`
- Run `npm install` to install all necessary dependencies
- Run `node Stargazers.js` and Voila! you are ready to go 😉

## Output

![Output Pic](https://i.imgur.com/eIecSza.png)

## Author(s)

Hi I'm [Madhav Jha](https://github.jhamadhav.com) author of this script.

## Disclaimer

### Why use the github token?

It is true that github api is freely available for use by public but it is restricted to 60 requests per hour and for repos with large number of stargazers this will exceed it's limit. So do get your [`Github Developer Token`](https://dev.to/gr2m/github-api-authentication-personal-access-tokens-53kd) before running this script
