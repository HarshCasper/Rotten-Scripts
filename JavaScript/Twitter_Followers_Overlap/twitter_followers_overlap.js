const prompt = require("prompt-sync")();
const twt = require("./twitterFunc")

const printLongArray = (arr, step = 100) => {
    if (arr.length <= 0) {
        return 0;
    }
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
    let arr1IDs = arr1.map(user => user.id);
    let arr2IDs = arr2.map(user => user.id);
    let overlap = []
    let overlapIDs = []

    // from arr1IDs -> arr2IDs
    for (let i = 0; i < arr1IDs.length; i++) {
        if (arr2IDs.indexOf(arr1IDs[i]) != -1 && overlapIDs.indexOf(arr1IDs[i]) == -1) {
            overlapIDs.push(arr1IDs[i])
            overlap.push(arr1[i]);
        }
    };

    // from arr2IDs -> arr1IDs
    for (let i = 0; i < arr2IDs.length; i++) {
        if (arr1IDs.indexOf(arr2IDs[i]) != -1 && overlapIDs.indexOf(arr2IDs[i]) == -1) {
            overlapIDs.push(arr2IDs[i])
            overlap.push(arr2[i]);
        }
    };
    return overlap;
}

const init = async () => {
    console.log("\n===============================");
    console.log("---Twitter Followers Overlap---");
    console.log("===============================\n");

    let user1 = prompt("Enter first username : ");
    let user2 = prompt("Enter second username : ");

    console.log("\nFetching...Data....Please..Wait...!\n");

    let user1ID = await twt.getUserId(user1)
    let user2ID = await twt.getUserId(user2)

    let user1Followers = await twt.getFollowers(user1ID["data"][0].id);
    let user2Followers = await twt.getFollowers(user2ID["data"][0].id);

    let overlapFollowers = getOverlappingFollowers(user1Followers, user2Followers);

    console.log(`There are ${overlapFollowers.length} Overlapping followers!!! \n`);
    printLongArray(overlapFollowers);
    console.log("\n---END---\n");

}

// entry function
init()
