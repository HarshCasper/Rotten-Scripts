const prompt = require("prompt-sync")();
const api = require("./apiTokens")
const twt = require("./twitterFunc")

const init = () => {
    /**
     * 1. ask names of two user
     * 2. get their followers
     * 3. compare them and get the overlap
     * 4. output the overlap
     */

    let user1 = prompt("Enter first username : ");
    let user2 = prompt("Enter second username : ");

    let user1Followers = twt.getFollowers();
    let user2Followers = twt.getFollowers();

    let overlapFollowers = getOverlappingFollowers();

    console.log("===============================");
    console.log("---Twitter Followers Overlap---");
    console.log("===============================");

    console.log("\n\nOverlapping followers are : \n");
    printLongArray(overlapFollowers);

}