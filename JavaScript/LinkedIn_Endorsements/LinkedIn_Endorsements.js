const prompt = require("prompt-sync")()
const scrapper = require("./scrapper")
const chalk = require("chalk")

const displayEndorsements = (data) => {
    for (let i = 0; i < data.length; i++) {

        console.log(`${i + 1}. ${chalk.yellow(data[i]["skill"])}`);
        console.log(`Endorsements: ${chalk.yellow(data[i]["number"])}`);
        console.log(`People:`);
        for (let j = 0; j < data[i]["people"].length; j++) {
            console.log(`\t${chalk.green(data[i]["people"][j])}`);
        }
        console.log("\n");

    }
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

    let profileLink = "https://www.linkedin.com/in/kunal-kushwaha/"//prompt("Enter LinkedIn profile link : ")

    let endorsements = await scrapper.getEndorsements(profileLink)

    console.log("The Endorsement data is as follows:\n");
    displayEndorsements(endorsements)

    console.log("\n---END---\n")
}

// entry function
init()
