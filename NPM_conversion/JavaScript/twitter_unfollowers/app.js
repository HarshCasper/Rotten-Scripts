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
    console.log(`Username : ${user.name} \nuserID : ${user.id}`);
}

const getUnfollowers = (current, fromDB) => {
    // separate usernames from the json array using map
    tempCurrent = current.map((user) => {
        return user.name;
    })
    tempFromDB = fromDB.map((user) => {
        return user.name;
    })

    // new list to store users that have unfollowed the user
    let unfollows = [];
    tempFromDB.forEach(user => {
        if (tempCurrent.indexOf(user) == -1) {
            unfollows.push(user);
        }
    });

    return unfollows;
}

const getDate = () => {
    let d = new Date();
    return `${d.getDate()}/${d.getMonth() + 1}/${d.getFullYear()}`
}

const updateDB = (dbData, currentData, unfollows) => {

    // assign current new user followers changes to db
    dbData[currentData.name]["followers"] = currentData["followers"];
    if (unfollows > 0) {
        let d = getDate();
        let newCheck = {
            "On-Date": d,
            "People-unfollowed": unfollows
        }
        // update time
        dbData[currentData.name].time = d;
        // make history of checking
        dbData[currentData.name]["history"].push(newCheck);
    }
    // write the data into the db
    db.write(dbFileLoc, dbData);
    return dbData;
}
const init = async () => {

    let username = prompt("Enter Twitter Username : "); //this info will be taken through input
    let user = await getUserData(username)
    let dbData = db.read(dbFileLoc);
    dbData = (dbData === "" || dbData.length == 0) ? "{}" : dbData;
    dbData = JSON.parse(dbData);

    if (Object.prototype.hasOwnProperty.call(dbData, user.name)) {
        // display basic info
        displayUser(user);

        // get list of people that have unfollowed you
        let people = getUnfollowers(user.followers, dbData[user.name]["followers"]);

        // displaying their number
        console.log(`\nNOTE : ${people.length} people unfollowed you(him/her) After ${dbData[user.name].time}`);

        // display their names
        if (people.length > 0) {
            console.log(`\nThose are(is) : `);
            console.table(people);
        }

        // to update the db with new data
        dbData = updateDB(dbData, user, people.length);

        if (dbData[user.name]["history"].length > 0) {
            console.log(`\Query history is as follows :`);
            console.table(dbData[user.name]["history"]);
        }
    } else {

        // assign current new user to db
        dbData[user.name] = user;
        // add date of addition
        dbData[user.name].time = getDate();
        // make history of checking
        dbData[user.name].history = [];
        // write the data into the db
        db.write(dbFileLoc, dbData);

        // inform us about the user not being in the db
        console.log("\nNOTE : User didn't exist! Now it has been added to DB.\nCheck after some time!!!");
    }
}
init();
