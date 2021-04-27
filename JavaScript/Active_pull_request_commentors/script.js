const fetch = require("node-fetch");
const createCsvWriter = require("csv-writer").createObjectCsvWriter;
require("dotenv").config();

let input = process.argv.slice(2);
let OWNER = input[0];
let REPO_NAME = input[1];
let NO_OF_REQUEST = input[2];
let obj;
const query = `query {
    repository(owner: "${OWNER}", name: "${REPO_NAME}") {
      url
      pullRequests(first:${NO_OF_REQUEST}, states:OPEN) {
        nodes {
          number
          url
          state
          author {
            login
            url
          }
          comments(first:100) {
            nodes {
              author {
                login
              }
              bodyText
            }
          }
        }
      }
    }
  }
  `;

(async function () {
  let res;
  try {
    res = await fetch("https://api.github.com/graphql", {
      method: "POST",
      body: JSON.stringify({ query }),
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${process.env.ACCESS_TOKEN}`,
      },
    });
    let body = await res.text();
    obj = JSON.parse(body);
    const csvWriter = createCsvWriter({
      path: "output.csv",
      header: [
        { id: "repo", title: "Repository" },
        { id: "PR", title: "PR No." },
        { id: "url", title: `URL` },
        { id: "comments", title: "comments" },
        { id: "author", title: "username of commentor" },
      ],
    });
    let data = [];
    let repo = obj.data.repository.url;
    let node = obj.data.repository.pullRequests.nodes;
    for (let i = 0; i < node.length; i++) {
      let n = node[i];
      let c = n.comments.nodes;
      for (let j = 0; j < c.length; j++) {
        let d = {
          repo: `${repo}`,
          PR: `${node[i].number}`,
          url: `${node[i].url}`,
          comments: `${c[j].bodyText}`,
          author: `${c[j].author.login}`,
        };
        data.push(d);
      }
    }
    csvWriter
      .writeRecords(data)
      .then(() => console.log("The CSV file was written successfully"));
  } catch (err) {
    console.log(err);
  }
})();
