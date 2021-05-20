# Github_Good_First_Issues

- **Github_Good_First_Issues** is a script to scrap `Good First Issues` from GitHub Repositories.
- It uses Github API to fetch repo and issues.
- Then displays them to the user. 

## Methods to fetch repositories

There are 3 ways to fetch repositories
1. `DB.js` file in the folder *(That can be overwritten by the user)*
2. [Github Trending Page](https://github.com/trending)
3. Starred repositories of a user *(User input)*

## Setup instructions

- Get your [`Github Developer Token`](https://dev.to/gr2m/github-api-authentication-personal-access-tokens-53kd) and follow the steps there to generate your **Token key**
- In a file named `token.js` paste the token.
- Open terminal and do the following : 
- `cd Rotten-Scripts\JavaScript\Github_Good_First_Issues`
- Run `npm install` to install all necessary dependencies
- Run `node Github_Good_First_Issues.js` and Voila! you are ready to go 😉

## Output

### Method 1: via DB

![ Method 1](https://i.imgur.com/eeAq9FN.png)

### Method 2: Github Trending

![ Method 2.1](https://i.imgur.com/HFlGh6j.png)
![ Method 2.2](https://i.imgur.com/3u8hXnv.png)

### Method 3: Starred repo(s) from user

![ Method 3](https://i.imgur.com/WJaCm5F.png)

## Author(s)

Hi I'm [Madhav Jha](https://github.com/jhamadhav) author of this script.

## Disclaimer

### Why use the github token?

It is true that github api is freely available for use by public but it is restricted to 60 requests per hour and for repositories with large number of issues this will exceed it's limit.
So do get your [`Github Developer Token`](https://dev.to/gr2m/github-api-authentication-personal-access-tokens-53kd) before running this script
