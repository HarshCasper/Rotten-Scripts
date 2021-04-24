const prompt = require("prompt-sync")()
const scrapper = require("./scrapper")
const chalk = require("chalk")

const displayEndorsements = (data) => {

}

const init = async () => {
    /**
     * 1. get LinkedIn profile link
     * 2. scrape endorsements
     * 3. display them
     */
    console.log("\n===================================");
    console.log("---LinkedIn Endorsement scrapper---");
    console.log("===================================\n");

    let profileLink = prompt("Enter LinkedIn profile link : ")

    let endorsements = await scrapper.getEndorsements(profileLink)
    displayEndorsements()

    console.log("\n---END---\n")
}

// entry function
init()
