// Script to track recent unfollowers on github using github api
// Author: vismitap

const prompt = require("prompt-sync")();
const Username = prompt("What is your Github Username? : ");

// require node-fetch
const node_fetch = require("node-fetch");

//require fs for memory of old and updated data
const fs = require("fs");

// require diff to find the diff
let url = `https://api.github.com/users/${Username}/followers`;

let current = JSON.parse(fs.readFileSync("old.json"));
console.table(current);
node_fetch(url)
  .then((res) => res.json())
  .then((out) => {
    let i = 0;
    let set = new Set();

    for (i in out) {
      set.add(out[i]["login"]);
    }

    if (current.length == 0) {
      console.log("Run for the first time.");
    } else {
      const unfollowers = current.filter((e) => !set.has(e));
      console.table(unfollowers);
    }
    fs.writeFileSync("old.json", JSON.stringify(Array.from(set)));
  })
  .catch((err) => console.log(err));