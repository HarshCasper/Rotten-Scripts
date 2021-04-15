const prompt = require("prompt-sync")();
const github = require("./githubFunc")
const db = require("./dbFunc")
const dbFileLoc = "db.json";

const getUserInfo = async (arr) => {

    let res = []
    for (let i = 0; i < arr.length; i++) {
        let userData = await github.getUserData(arr[i])
        let obj = {
            "id": arr[i],
            "name": userData.name,
            "email": userData.email,
            "location": userData.location
        }
        res[i] = obj;
    }
    return res;
}

const addNewData = async (dbData, username, repoName, stargazers) => {
    stargazers = await getUserInfo(stargazers);

    let data = {
        "stargazers": stargazers,
        "unstargazers": [],
        "time": getDate()
    }
    if (!dbData.hasOwnProperty(username)) {
        dbData[username] = {}
    }
    dbData[username][repoName] = data;
    db.write(dbFileLoc, dbData);
}

const init = async () => {
    //these info will be taken through input
    let username = prompt("Enter Github Username : ");
    let repoName = prompt("Enter Repo name : ");

    let stargazers = await github.getUsers(username, repoName);
    stargazers = stargazers.map(user => user.login)

    let dbData = db.read(dbFileLoc);
    dbData = (dbData === "" || dbData.length == 0) ? "{}" : dbData;
    dbData = JSON.parse(dbData);

    // if user exits
    if (dbData.hasOwnProperty(username) && dbData[username].hasOwnProperty(repoName)) {


    } else {
        // if user's repo exists
        console.log("user doesn't exist");
        addNewData(dbData, username, repoName, stargazers)
        console.log("New data added!!");
    }
}

const getDate = () => {
    let d = new Date();
    return `${d.getDate()}/${d.getMonth() + 1}/${d.getFullYear()}`
}

// main function
console.log(`
======================
------Stargazers------
======================\n`);
init()