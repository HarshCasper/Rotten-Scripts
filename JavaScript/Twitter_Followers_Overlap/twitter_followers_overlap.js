const prompt = require("prompt-sync")();
const twt = require("./twitterFunc")

const printLongArray = (arr, step = 100) => {
    let start = 0, end = 0;
    end = Math.min(step, arr.length);

    let userInp = prompt(`Do you want to see list from ${start} to ${end} (y/n): `) || "n"
    while (userInp == "y" && end <= arr.length && start != end) {
        subArr = arr.slice(start, end)
        console.table(subArr)
        start = end;
        end = Math.min(end + step, arr.length)
        if (start == end) {
            break;
        }
        userInp = prompt(`Do you want to see list from ${start} to ${end} (y/n): `) || "n"
    }
}

const getOverlappingFollowers = (arr1, arr2) => {

}

const init = () => {
    /**
     * 1. ask names of two user
     * 2. get their followers
     * 3. compare them and get the overlap
     * 4. output the overlap
     */

    let user1 = prompt("Enter first username : ");
    let user2 = prompt("Enter second username : ");

    let user1Followers = twt.getFollowers(user1);
    let user2Followers = twt.getFollowers(user2);

    let overlapFollowers = getOverlappingFollowers(user1Followers, user2Followers);

    console.log("===============================");
    console.log("---Twitter Followers Overlap---");
    console.log("===============================");

    console.log("\n\nOverlapping followers are : \n");
    printLongArray(overlapFollowers);

}

// entry function
init()
