const prompt = require("prompt-sync")()
const scrapper = require("./scrapper")
const chalk = require("chalk")

const displayEndorsements = (data) => {
    for (let i = 0; i < data.length; i++) {

        console.log(`${i + 1}. ${chalk.yellow(data[i]["skill"])}`);
        console.log(`Endorsements: ${chalk.yellow(data[i]["number"])}`);
        if (data[i]["number"] != 0) {
            console.log(`People:`);
        }

        let col = 3
        for (let j = 0; j < data[i]["people"].length; j += col) {
            let str = ``
            for (let k = 0; k < col && j + k < data[i]["people"].length; k++) {
                str += `${chalk.green(data[i]["people"][j + k])}, `
            }
            console.log(`  ${chalk.green(str)}`);
        }

        console.log("\n");
    }
}

const init = async () => {
    console.log("\n===================================");
    console.log("---LinkedIn Endorsement scrapper---");
    console.log("===================================\n");

    let profileLink = prompt("Enter LinkedIn profile link : ")

    let endorsements = await scrapper.getEndorsements(profileLink)

    console.log("\nThe Endorsement data is as follows:\n");
    displayEndorsements(endorsements)

    console.log("\n---END---\n")
}

// entry function
init()
