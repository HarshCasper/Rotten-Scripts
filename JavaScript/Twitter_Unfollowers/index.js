const prompt = require("prompt-sync")();
const db = require("./dbFunc")
const api = require("./apiTokens")
const twt = require("./twitterFunc")
const dbFileLoc = "db.json";

// api data
const bearerToken = api.data.bearer;

const getUserData = async (username) => {
    let user = new Object();
    user.name = username;
    let res = await twt.getUserId(user.name, bearerToken)
    user.id = res.data[0].id;
    user.followers = await twt.getFollowers(user.id, bearerToken);
    return user;
}

const displayUser = (user) => {
    console.log("\nUser Info :");
    console.log(`Name : ${user.name} ID : ${user.id}`);
    // console.log(user);
}

const getUnfollowers = (current, fromDB) => {
    current = current.map((user) => {
        return user.name;
    })
    fromDB = fromDB.map((user) => {
        return user.name;
    })
    // console.log(current);
    // console.log(fromDB);
    let unfollows = [];
    fromDB.forEach(user => {
        if (current.indexOf(user) == -1) {
            unfollows.push(user);
        }
    });
    return unfollows;
}
const init = async () => {

    let username = prompt("Enter Twitter Username : "); //this info will be taken through input
    let user = await getUserData(username)
    let dbData = db.read(dbFileLoc);
    dbData = (dbData === "" || dbData.length == 0) ? "{}" : dbData;
    dbData = JSON.parse(dbData);

    if (dbData.hasOwnProperty(user.name)) {
        displayUser(user);
        let people = getUnfollowers(user.followers, dbData[user.name]["followers"]);
        console.log(people);
        console.log(`${people.length} people unfollowed you since ${dbData[user.name]["time"]}`);
    } else {
        dbData[user.name] = user;

        let d = new Date();
        dbData[user.name].time = `${d.getDate()}/${d.getMonth() + 1}/${d.getFullYear()}`;
        db.write(dbFileLoc, dbData);
        console.log("User didn't exist! Now it has been added to DB.\nCheck after some time!!!");
    }
}

init();

