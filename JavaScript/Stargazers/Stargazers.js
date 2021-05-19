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
        console.log(`${i} user added`);
    }
    return res;
}

const addNewData = async (dbData, username, repoName, stargazers) => {
    stargazers = await getUserInfo(stargazers);

    let data = {
        "stargazers": stargazers,
        "time": getDate()
    }
    if (!dbData.hasOwnProperty(username)) {
        dbData[username] = {}
    }
    dbData[username][repoName] = data;
    db.write(dbFileLoc, dbData);
}
const getUnstargazers = (prev, stargazers) => {
    let prevName = prev.map(user => user.id);
    let unstargazers = []
    let delArr = [];
    for (let i = 0; i < prevName.length; i++) {
        if (stargazers.indexOf(prevName[i]) == -1) {
            unstargazers.push(prev[i])
            delArr.push(i)
        }
    }
    return unstargazers;
}
const getNewStargazers = async (prev, stargazers) => {
    let prevName = prev.map(user => user.id);
    let newStargazers = []

    for (let i = 0; i < stargazers.length; i++) {
        if (prevName.indexOf(stargazers[i]) == -1) {
            newStargazers.push(stargazers[i])
        }
    }
    console.log(`\n${newStargazers.length} people have recently starred this repo.`);
    if (newStargazers.length > 0) {
        console.log("Adding them to the DB.....please wait....");
    }
    newStargazers = await getUserInfo(newStargazers)
    return newStargazers;
}
const addNewStargazers = (username, repoName, dbData, newStargazers) => {
    let arr = dbData[username][repoName]["stargazers"]
    arr = [...arr, ...newStargazers]

    dbData[username][repoName]["stargazers"] = arr;
    db.write(dbFileLoc, dbData)
}

const printLongArray = (arr, step = 100) => {
    let start = 0, end = 0;
    end = Math.min(step, arr.length);

    let userInp = prompt(`Do you want to see list from ${start} to ${end} (y/n): `) || "n"
    while (userInp == "y" && end <= arr.length && start != end) {
        subArr = arr.slice(start, end)
        console.table(subArr, ["name", "email", "location"])
        start = end;
        end = Math.min(end + step, arr.length)
        if (start == end) {
            break;
        }
        userInp = prompt(`Do you want to see list from ${start} to ${end} (y/n): `) || "n"
    }
}

const delUnStargazers = (username, repoName, dbData, unstargazers) => {
    let arr = dbData[username][repoName]["stargazers"]
    idArr = arr.map(user => user.id)
    unstargazers = unstargazers.map(user => user.id)

    for (let i = 0; i < unstargazers.length; i++) {
        let index = idArr.indexOf(unstargazers[i])
        arr.splice(index, 1);
        idArr.splice(index, 1);
    }
    dbData[username][repoName]["stargazers"] = arr;
    db.write(dbFileLoc, dbData)
}


const init = async () => {
    //these info will be taken through input
    let username = prompt("Enter Github Username: ");
    let repoName = prompt("Enter Repo name : ");

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
        console.log("\nINFO : \n");

        let currentStargazers = dbData[username][repoName]["stargazers"];
        // current DB
        console.log(`There are ${currentStargazers.length} that have currently starred this repo.`);

        // ask to print stargazers
        if (currentStargazers.length != 0) {
            printLongArray(currentStargazers, 100);
        }

        // people that unstarred
        let unstargazers = getUnstargazers(dbData[username][repoName]["stargazers"], stargazers);
        console.log(`\n${unstargazers.length} people have unstarred this repo since ${dbData[username][repoName]["time"]}`);

        // ask to print unstargazers
        if (unstargazers.length != 0) {
            printLongArray(unstargazers, 100);
        }

        // delete people that have unStarred
        delUnStargazers(username, repoName, dbData, unstargazers)

        // new people that have starred
        let newStargazers = await getNewStargazers(dbData[username][repoName]["stargazers"], stargazers);

        // ask to print newStargazers
        if (newStargazers.length != 0) {
            printLongArray(newStargazers, 100);
        }

        // new people that have starred
        if (newStargazers.length != 0) {
            addNewStargazers(username, repoName, dbData, newStargazers)
        }

        // update time
        dbData[username][repoName]["time"] = getDate()
        db.write(dbFileLoc, dbData)

    } else {
        // if user's repo exists
        console.log("\nuser doesn't exist");
        console.log(`Fetching ${stargazers.length} user data.... please wait ....`);
        addNewData(dbData, username, repoName, stargazers)
        console.log("New data added!!");
    }

    console.log("\n---End---\n");
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
