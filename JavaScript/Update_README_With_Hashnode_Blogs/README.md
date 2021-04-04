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
//in update_readme.jsline 34
/(?<=Latest Blogs\n)[\s\S]*(?=\#\#\ This Point Won't Be Edited)/gim,
```

This is very important thing. Used regular expression so that script modify only the necessary part not the whole `README.md`. If you want to write other things instead of **Latest Blogs** (EX: My Blogs) you have to modify regular expressions like `/(?<=My Blogs\n)[\s\S]*(?=\#\#\ This Point Won't Be Edited)/gim,`
Next most important thing is upto which point will be replaced. Suppose you have a Section My Blogs & # Skills, you want to replace texts between them then you have to modify like this `/(?<=My Blogs\n)[\s\S]*(?=\#\ Skills)/gim,` .
⚡️ For the starting point (here `My Blogs`) doesn't need to consider what is before it like ##My Blogs or ##### MY Blogs etc.
If you are beginner in regular expression [RegExr](https://regexr.com/) will help you.

- Go to [RegExr](https://regexr.com/)
- Paste your `README.md` text below text section
- Paste the `/(?<=Latest Blogs\n)[\s\S]*(?=\#\#\ This Point Won't Be Edited)/gim` under expression
- Change those mentioned changes and see which texts are selcted those texts will be replaced.

🔥🔥🔥
Current script set to show 3 latest posts if you want to set more than three then change these lines

```js
//If you want to set 5 posts
const posts = response.data.user.publication.posts.slice(0, 5); //in update_readme.js, line 25
//in update_readme.js, line 26
const postsToShow = `\n - [${posts[0].title}](<you hashnode blog URL>/${posts[0].slug})\n - [${posts[1].title}](<you hashnode blog URL>/${posts[1].slug})\n - [${posts[2].title}](<you hashnode blog URL>/${posts[2].slug})\n - [${posts[3].title}](<you hashnode blog URL>/${posts[3].slug})\n - [${posts[4].title}](<you hashnode blog URL>/${posts[4].slug})\n\n`;
```

🌟️ Check demo [update_readme.js](https://paste.ubuntu.com/p/rXN9DwcBPR/)
