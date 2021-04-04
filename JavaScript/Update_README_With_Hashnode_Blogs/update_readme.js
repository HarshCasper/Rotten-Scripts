const fetch = require("node-fetch");
const fs = require("fs");
const query = `
    {
      user(username: "<your Hashnode username>") {
        publication {
          posts{
            slug
            title
          }
        }
      }
    }
  `;

const fetchPosts = async () => {
  const result = await fetch("https://api.hashnode.com", {
    method: "POST",
    headers: {
      "Content-type": "application/json",
    },
    body: JSON.stringify({ query }),
  });
  const response = await result.json();
  const posts = response.data.user.publication.posts.slice(0, 3);
  const postsToShow = `\n - [${posts[0].title}](<you hashnode blog URL>/${posts[0].slug})\n - [${posts[1].title}](<you hashnode blog URL>/${posts[1].slug})\n - [${posts[2].title}](<you hashnode blog URL>/${posts[2].slug})\n\n`;
  fs.readFile("README.md", "utf-8", (err, data) => {
    if (err) {
      throw err;
    }
    console.log(postsToShow);
    const updatedMd = data.replace(
      // To replace texts or blogs between Latest Blogs and Contributors Section
      /(?<=Latest Blogs\n)[\s\S]*(?=\#\#\ This Point Won't Be Edited)/gim,
      postsToShow
    );
    fs.writeFile("README.md", updatedMd, "utf-8", (err) => {
      if (err) {
        throw err;
      }
    });
  });
};
fetchPosts();
