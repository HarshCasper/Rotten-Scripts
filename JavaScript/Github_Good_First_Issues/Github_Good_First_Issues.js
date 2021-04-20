const prompt = require("prompt-sync")()

const init = () => {
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


    console.log("1. From the JSON file in the folder (enter 1)")
    console.log("2. From the trending page of Github (enter 2)")
    console.log("3. From the starred repo of an user (enter 3)")
    let method = prompt("Choose method to fetch repo : ")

    let username = null;
    if (Number(method) == 3) {
        username = prompt("\nEnter github username : ")
    }

    let repo = getRepoViaMethod(method, username)
    let issues = getIssues(repo)

    printIssues(issues);
}

// entry function
init();
