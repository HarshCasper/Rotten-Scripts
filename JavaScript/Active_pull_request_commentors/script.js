const fetch = require("node-fetch");
const createCsvWriter = require("csv-writer").createObjectCsvWriter;

let OWNER = `HarshCasper`; // replace with repository's owner username
let REPO_NAME = `Rotten-Scripts`; // replace with repositort's name
let NO_OF_REQUEST = 10; // replace with no. of latest Active pull request data you want to access
let obj;
const accessToken = ""; // replace with your own github access token
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

fetch("https://api.github.com/graphql", {
  method: "POST",
  body: JSON.stringify({ query }),
  headers: {
    "Content-Type": "application/json",
    Authorization: `Bearer ${accessToken}`,
  },
})
  .then((res) => res.text())
  .then((body) => {
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
  })
  .catch((error) => console.error(error));
