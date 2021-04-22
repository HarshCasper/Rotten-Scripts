const prompt = require("prompt-sync")()
const scrapper = require("./scrapper")
const chalk = require("chalk")
const urlParser = require("url-parse")

const displayHackathonsInfo = (obj) => {
    console.log(`\nHACKATHON : ${chalk.yellow(obj.title)}`);
    console.log(`DESCRIPTION : ${chalk.green(obj.description)}\n`);
}

const displayProjectInfo = () => {

}

const init = async () => {
    /*
     * 1.get hackathons link as input
     * 2.get hackathons html page data
     * 3.extract project links from page
     * 4.get project info
     * 5.display project data 
     */
    console.log("\n=================================");
    console.log("---DevPost Hackathons Scrapper---");
    console.log("=================================\n");

    let hackathonsLink = "https://hack-js.devpost.com/?ref_feature=challenge&ref_medium=discover"//prompt("Enter DevPost link : ")

    let parsedUrl = urlParser(hackathonsLink)
    hackathonsLink = "https://" + parsedUrl.hostname

    console.log("\nFetching..Data....Please..Wait...!\n");

    let hackathonsData = await scrapper.getHackathonsData(hackathonsLink)
    displayHackathonsInfo(hackathonsData)

    let hackathonsProjectsURL = `${hackathonsLink} + /project-gallery`
    let projectLinks = await scrapper.getProjects(hackathonsProjectsURL)
    let projectData = await scrapper.getProjectsData(projectLinks)

    displayProjectInfo(projectData)
}

// entry function
init()
