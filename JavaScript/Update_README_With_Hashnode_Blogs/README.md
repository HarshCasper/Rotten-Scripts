# About

This script helps to show recent blogs published by anyone in **Hashnode** on [GitHub Profile README.md](https://docs.github.com/en/github/setting-up-and-managing-your-github-profile/managing-your-profile-readme). The main benefit of using the script is the whole README.md won't be updated. It will update only what you select to update. So, you can use it to update any place of your README.md by blogs. The script won't update the README.md unnecessarily when it will be scheduled to run. If any differences are found from the current version of README.md only then it will update that differenced portions only.

This script is not limited to use in `GitHub Profile README.md` only, it can be customized and in use other places too.

# Initial Setup

- Create a folder name `.github`
- Create a folder name `workflows` inside `.github`
- Copy the file `recent_blogs.yml` to the `workflows` folder
- Copy the `update_readme.js` file to the root folder
- Copy the text of `DemoReadMe.md` to your `README.md` and place it any where

# Modification

🔥
Currently set to check for new blogs for every 5 hour. If you are not happy with it you can modify it.

`recent_blogs.yml` line 6

```yml
- cron: "* */5 * * *"
```

But modifying **cron** schedule is little bit tricky for beginners. Go to [crontab guru](https://crontab.guru/), you will be able to change **cron** schedule very easily

🔥🔥

```js
//in update_readme.jsline 58
/(?<=Latest Blogs\n)[\s\S]*(?=\#\#\ This Point Won't Be Edited)/gim,
```

This is very important thing. Used regular expression so that script modify only the necessary part not the whole `README.md`. If you want to write other things instead of **Latest Blogs** (EX: My Blogs) you have to modify regular expressions like `/(?<=My Blogs\n)[\s\S]*(?=\#\#\ This Point Won't Be Edited)/gim,`
Next most important thing is upto which point will be updated. Suppose you have a Section My Blogs & # Skills, you want to update texts between them then you have to modify like this `/(?<=My Blogs\n)[\s\S]*(?=\#\ Skills)/gim,` .

⚡️ For the starting point (here `My Blogs`) doesn't need to consider what is before it like ##My Blogs or ##### MY Blogs etc.
If you are beginner in regular expression [RegExr](https://regexr.com/) will help you.

- Go to [RegExr](https://regexr.com/)
- Paste your `README.md` text below text section
- Paste the `/(?<=Latest Blogs\n)[\s\S]*(?=\#\#\ This Point Won't Be Edited)/gim` under expression
- Change those mentioned changes and see which portions are selcted those portions will be updated if found any changes.

🔥🔥🔥
Current script set to show 3 latest posts if you want to set more than three then change these lines.

```js
//If you want to set 5 posts
const numberOfPosts = 5; //in update_readme.js <- line 3
```

⚠️ At the time of writing this, **Hashnode API** gives max latest 6 blogs properties as a response.

🌟️ Check demo [update_readme.js](https://pastebin.ubuntu.com/p/96kCqgmPK6/)
