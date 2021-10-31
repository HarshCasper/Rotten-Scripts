import fetch from "node-fetch";
import readline from "readline";

const _interface = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const userData = {}

_interface.question('Enter your GitHub username: ', name => {
    fetch(`https://api.github.com/users/${name}`)
    .then((res) => res.json())
    .then((data) => {
        if(data.message === "Not Found"){
            console.error("Invalid Username")
            process.exit(0)
        }
        userData["Username"] = data.login
        userData["Location"] = data.location
        userData["Bio"] = data.bio
        userData["Repositories"] = data.public_repos
        userData["Followers"] = data.followers
        userData["Following"] = data.following
        console.table(userData)
    })

    _interface.close()
});