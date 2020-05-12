# Edit Webpage

To all the Web Developers here, this is an interesting Code Snippet you can play with 😍

This Code Snippet allows you to edit any content on a particular Webpage without using Inspect Elements and Dev Tools. Just open up any particular Webpage and go to the URL bar and type in: 

```
javascript: /* Get all the Elements using DOM and store it onto the variable 'a' */ a = document.getElementsByTagName("*"); /* With each variable, add the HTML aiitribute that contenteditable is true */ for (i = 0; i < a.length; i++){ a[i].setAttribute("contenteditable", "true"); }; /* Now the attributes related to href are removed from the <a> tags */ href = document.getElementsByTagName("a"); for (i = 0; i < href.length; i++) { href[i].removeAttribute("href"); }
```

Play around with it and suggest how helpful it was!

![image](https://nimbus-screenshots.s3.amazonaws.com/s/ce03ee0fb0d405b6d4acf8a1adff0d9f.png)
