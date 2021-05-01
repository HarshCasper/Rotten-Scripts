const fetch = require("node-fetch");
const fs = require("fs");
const numberOfPosts = 3;
const blogURL = "your Hashnode blog URL";
const username = "your Hashnode username";

const query = `
    {
      user(username: "${username}") {
        publication {
          posts{
            slug
            title
          }
        }
      }
    }
  `;

const fetchPosts = async (numberOfPosts) => {
  const result = await fetch("https://api.hashnode.com", {
    method: "POST",
    headers: {
      "Content-type": "application/json",
    },
    body: JSON.stringify({ query }),
  });
  const response = await result.json();
  
  //This log will be printed in the action's log, under the Run Script section
  console.log(
    "Posts received from Hashnode API as a response:",
    response.data.user.publication.posts
  );

  const posts = response.data.user.publication.posts.slice(0, numberOfPosts);
  let postsToShow = "";
  for (i = 0; i < numberOfPosts && i < response.data.user.publication.posts.length; i++) {
    if (i != numberOfPosts - 1) {
      postsToShow += `\n - [${posts[i].title}](${blogURL}/${posts[i].slug})`;
    } else {
      postsToShow += `\n - [${posts[i].title}](${blogURL}/${posts[i].slug})\n`;
    }
  }

  //This log will be printed in the action's log, under the Run Script section
  console.log(
    "If any changes found among these lines, will be updated in README.md:",
    postsToShow
  );

  fs.readFile("README.md", "utf-8", (err, data) => {
    if (err) {
      throw err;
    }
    const updatedMd = data.replace(
      // To replace texts or blogs between `Latest Blogs` and `## This Point Won't Be Edited` Section
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
fetchPosts(numberOfPosts);
