const prompt = require("prompt-sync")()
const git = require("./githubFunc")
const chalk = require("chalk")

const printIssues = (arr) => {
    for (let i = 0; i < arr.length; i++) {
        console.log(chalk.yellow(`\n\n${i + 1}. ${arr[i]["repoOwner"]}/${arr[i]["repoName"]} : `))

        let issues = arr[i]["issues"]
        if (issues.length == 0) {
            console.log(chalk.red("  None found!!"))
            continue
        }
        for (let j = 0; j < issues.length; j++) {
            console.log(chalk.blue(`\n  ${j + 1}. ${issues[j]["title"]} `))
            console.log(`  URL: ${chalk.green(issues[j]["url"])} `)
        }
    }
}

const init = async () => {
    /**
     * 1. ask user from three options
     * a. Having a JSON File where all the repositories are stored.
     * b. Scrapping from the top repositories that are trending on GitHub Explore
     * c. Scrapping from the repo that we/or someone else has starred
     * 
     * 2. fetch repo
     * 3. fetch issues with "Good first issues" label
     * 4. display them
    */
    console.log("\n================================")
    console.log("----Github Good First Issues----")
    console.log("================================\n")


    console.log("1. From the JSON file in the folder")
    console.log("2. From the trending page of Github")
    console.log("3. From the starred repo of an user")
    let method = prompt("Choose method to fetch repo : ")

    let username = null;
    if (Number(method) == 3) {
        username = prompt("Enter github username : ")
    }

    console.log("\n...Fetching Data....Please wait...\n");
    let repo = await git.getRepoViaMethod(method, username)
    let issues = await git.getIssues(repo)

    console.log("\nINFO : ");
    printIssues(issues);

    console.log("\n---END---\n");
}

// entry function
init();
