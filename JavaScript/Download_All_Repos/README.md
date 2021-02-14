# Nodejs Script to Download all user Repositories

## About

Github being the top choice for open source and storing our Projects code, it becomes very difficult for us to clone each and every Repository. This is time consuming when we want to have a copy of all our github repositories in our PC. So keeping this in mind I have developed a script to download all your github repositories(Public) in once!

## Explanation of code

- Github api is used to fetch all user repositories(https://api.github.com/user/[username]/repos)
- We are using shelljs and git to clone individual repositories
- All public repositories are fetched using https get module
- We are storing all repositories in a folder name _Repositories_username_

## To run the code

- Clone the folder
- Inside the folder open command line and run
- npm install
- Then _node downloadAllRepos your_username_

**Your Repositories will start downloading**

## Output

![image](https://i.imgur.com/LLJGgZY.png)
**code by [Mohit Bhat](https://www.mbcse.co)**
