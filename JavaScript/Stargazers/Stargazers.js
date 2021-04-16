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
        console.log(`${i + 1} user added`);
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
const getUnstargazers = (dbData, stargazers) => {

}

const printLongArray = (arr, step = 100) => {
    let start = 0, end = 0;
    end = Math.min(step, arr.length);

    let userInp = prompt(`Do you want to see list from ${start} to ${end} (y/n): `) || "n"
    while (userInp == "y" && end <= arr.length && start < end) {
        subArr = arr.slice(start, end)
        console.table(subArr, ["name", "email", "location"])
        start = end;
        end = Math.min(end + step, arr.length)
        userInp = prompt(`Do you want to see list from ${start} to ${end} (y/n): `) || "n"
    }
}
const init = async () => {
    //these info will be taken through input
    let username = "HarshCasper"//prompt("Enter Github Username: ");
    let repoName = "Rotten-Scripts"//prompt("Enter Repo name : ");

    let stargazers = await github.getUsers(username, repoName);
    if (stargazers.message) {
        console.log("\nERROR : Either the User or the repo doesn't exist!!!");
        return 0;
    }
    stargazers = stargazers.map(user => user.login)

    let dbData = db.read(dbFileLoc);
    dbData = (dbData === "" || dbData.length == 0) ? "{}" : dbData;
    dbData = JSON.parse(dbData);

    // if user exits
    if (dbData.hasOwnProperty(username) && dbData[username].hasOwnProperty(repoName)) {
        console.log("INFO : \n");
        // current info
        // console.log(`${stargazers.length} people have starred this repo!`);

        // // people that unstared
        // let unstargazers = getUnstargazers(dbData, stargazers);
        // console.log(`${unstargazers} people have unstarred this repo since ${dbData[username][repoName]["time"]}`);

        printLongArray(dbData[username][repoName]["stargazers"], 100);

        // new people that have starred


    } else {
        // if user's repo exists
        console.log("user doesn't exist");
        // addNewData(dbData, username, repoName, stargazers)
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