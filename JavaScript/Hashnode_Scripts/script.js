// all requires
const fetch = require("node-fetch");
const ObjectsToCsv = require("objects-to-csv");

let page = 0;
let postCount = process.argv[2];

// Working Function
fetchPosts = async (postCount) => {
    let postsData = []; // stores posts
    let count = 0;
    let currentPostCount = 0;

    while (currentPostCount < postCount) {
        const query = `{
            storiesFeed(type:BEST
                page:${page}){
                title
                brief
                author{
                  name
                }
              }
        }`;

        const response = await fetch("https://api.hashnode.com", {
            method: "POST",
            headers: {
                "Content-type": "application/json",
            },
            body: JSON.stringify({
                query
            }),
        });

        const apiResponse = await response.json();

        let posts = apiResponse.data.storiesFeed;

        currentPostCount += posts.length;

        page++;

        for (let post of posts) {
            count++;

            let postObject = {};

            postObject["title"] = post["title"];

            postObject["brief"] = post["brief"].split("\n").join(" ");

            postObject["author"] = post.author["name"];

            postsData.push(postObject);

            if (count >= postCount) break;
        }
    }

    const csv = new ObjectsToCsv(postsData);

    await csv.toDisk("./output.csv");
};

fetchPosts(postCount);
