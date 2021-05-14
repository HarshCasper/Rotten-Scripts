const axios = require("axios");
const fs = require("fs");
require("dotenv").config();

const config = {
  headers: {
    Authorization: process.env.Authorization,
  },
};
var obj = {
  table: [],
};
const getDetails = async (username, repoName) => {
  const url = `https://api.github.com/repos/${username}/${repoName}/issues`;
  await axios
    .get(url, config)
    .then(async (result) => {
      result.data.map(async (issue) => {
        const issueCreator = issue.user.login;
        const issueAssignees = issue.assignees.map((assignee) => assignee);
        const issueOpenDate = new Date(issue.created_at);
        const issueState = issue.state;
        const issueClosedDate =
          issueState === "open"
            ? "Its not closed yet"
            : new Date(issue.closed_at);
        const issueContent = issue.body;
        let issueCommentorDetails;
        // debugger
        const commentsUrl = `${url}/${issue.number}/comments`;
        await axios
          .get(commentsUrl, config)
          .then(async (commentData) => {
            issueCommentorDetails = commentData.data.map((comment, index) => {
              return {
                number: index,
                commentorUserName: comment.user.login,
                commentBody: comment.body,
              };
            });
          })
          .catch((err) => {
            throw err;
          });
        const issueDetailsjson = {
          issueCreator: issueCreator,
          issueOpenDate: issueOpenDate,
          issueClosedDate: issueClosedDate,
          issueState: issueState,
          issueAssignees: issueAssignees,
          issueContent: issueContent,
          issueCommentorDetails: issueCommentorDetails,
        };
        obj.table.push(issueDetailsjson);
        const json = JSON.stringify(obj, null, 4);
        fs.writeFileSync("issueDetails.json", json, (err) => {
          if (err) throw err;
        });
      });
    })
    .catch((err) => {
      throw err;
    });
};
//Put your Username and RepoName you wanna test here
const user = "";
const repoName = "";
getDetails(user, repoName);
