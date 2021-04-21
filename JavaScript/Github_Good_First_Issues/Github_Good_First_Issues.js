const prompt = require("prompt-sync")()
const git = require("./githubFunc")

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
    console.log("\n================================");
    console.log("----Github Good First Issues----");
    console.log("================================\n");


    console.log("1. From the JSON file in the folder")
    console.log("2. From the trending page of Github")
    console.log("3. From the starred repo of an user")
    let method = prompt("Choose method to fetch repo : ")

    let username = null;
    if (Number(method) == 3) {
        console.log("\n")
        username = prompt("Enter github username : ")
    }

    let repo = await git.getRepoViaMethod(method, username)
    console.table(repo);
    // let issues = getIssues(repo)

    // printIssues(issues);
}

// entry function
init();
