// Script to track recent unfollowers on github using github api
// Author: vismitap

const prompt = require("prompt-sync")();
const Username = prompt("What is your Github Username? : ");

// require node-fetch
const node_fetch = require("node-fetch");

//require fs for memory of old and updated data
const fs = require("fs");

let url = `https://api.github.com/users/${Username}/followers`;

let current = JSON.parse(fs.readFileSync("Followers.json"));
console.table(current);

// fetch data and store in set
node_fetch(url)
  .then((res) => res.json())
  .then((out) => {
    let i = 0;
    let set = new Set();
    
    // find the followers username on github from the returned json by github API
    for (i in out) {
      set.add(out[i]["login"]);
    }

    if (current.length == 0) {
      console.log(`Hey ${Username}, 
      Welcome to Github_Unfollowers!
      On your way to know the unfollowers!
      Run the command once again!`);
    } else {
      const unfollowers = current.filter((e) => !set.has(e));
      console.log("The unfollowers are: ")
      console.table(unfollowers);
    }
    fs.writeFileSync("Followers.json", JSON.stringify(Array.from(set)));
  })
  .catch((err) => console.log(err));
