const express = require("express");
const axios = require("axios");
const fs = require("fs");
const getDetails = async (username, repoName) => {
  const url = `https://api.github.com/repos/${username}/${repoName}/issues`;
  await axios
    .get(url)
    .then(async (result) => {
      console.log(result);
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
        const commentsUrl = url + "/" + issue.number + "/comments";
        await axios
          .get(commentsUrl)
          .then((commentData) => {
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
        };

        //This is being added so to avoid all the content being placed on a single line and shouls come on
        //Separate limes
        const JSON_DATA = JSON.stringify(issueDetailsjson, null, 2);
        if (fs.existsSync("issueDetails.json")) {
          const stringifiedJson =
            "," + JSON_DATA;
          fs.appendFileSync("issueDetails.json", stringifiedJson);
        } else {
          const stringifiedJson =
            "[" + JSON_DATA+ "]";
          fs.writeFileSync("issueDetails.json");
        }
      });
    })
    .catch((err) => {
      console.log(err);
    });
};
//Put your Username and RepoName you wanna test here
const user = "";
const repoName = "";
getDetails(user, repoName);
