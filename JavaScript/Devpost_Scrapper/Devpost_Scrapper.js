const prompt = require("prompt-sync")()
const scrapper = require("./scrapper")
const chalk = require("chalk")
const urlParser = require("url-parse")

const displayHackathonsInfo = (obj) => {
    console.log(`\nHACKATHON : ${chalk.yellow(obj.title)}`);
    console.log(`DESCRIPTION : ${chalk.green(obj.description)}\n`);
}

const displayProjectInfo = (arr) => {
    for (let i = 0; i < arr.length; i++) {
        let project = arr[i]
        console.log(`\n${i + 1}. ${chalk.yellow(project.title)}`)
        console.log(`Description : ${chalk.green(project.description)}`)
        console.log(`Subtitle : ${chalk.green(project.subtitle)}`)
        if (project.techUsed.length == 0) {
            console.log("Tech-Used : " + chalk.red("None"));
        } else {
            console.log(`Tech-Used : ${chalk.green(project.techUsed)}`)
        }
        if (project.images.length == 0) {
            console.log("Images : " + chalk.red("None"));
        } else {
            console.log(`Images : ${chalk.green(project.images.join("\n"))}`)
        }
        console.log(`Link : ${chalk.blue(project.link)}`)
    }
}

const ran = (min = 0, max = 1) => {
    return Math.floor(Math.random() * (max - min) + min)
}

const displaySheets = (partition, data) => {
    let projectData = data
    let n = Math.ceil(projectData.length / partition)
    for (let i = 0; i < partition; i++) {
        console.log(chalk.yellow(`\nSheet ${i + 1} : `));
        for (let j = 0; j < n; j++) {
            if (projectData.length == 0) {
                break;
            }
            let index = ran(0, projectData.length)
            console.log(`${j + 1} : ${chalk.green(projectData[index].title)}`);
            console.log(`Link : ${chalk.blue(projectData[index].link)}`);
            projectData.splice(index, 1)
        }
    }
}

const init = async () => {
    console.log("\n=================================");
    console.log("---DevPost Hackathons Scrapper---");
    console.log("=================================\n");

    let hackathonsLink = prompt("Enter DevPost link : ")

    let parsedUrl = urlParser(hackathonsLink)
    hackathonsLink = "https://" + parsedUrl.hostname

    console.log("\nFetching..Data....Please..Wait...!\n");

    let hackathonsData = await scrapper.getHackathonsData(hackathonsLink)
    displayHackathonsInfo(hackathonsData)

    let hackathonsProjectsURL = hackathonsLink + "/project-gallery"
    let projectLinks = await scrapper.getProjects(hackathonsProjectsURL)

    if (projectLinks.length == 0) {
        console.log(chalk.red("\nNOTE : No projects found, Please wait till the hackathon ends and try again!!!\n"))
        console.log("\n---END---\n")
        return 0
    }
    console.log(`${chalk.yellow(projectLinks.length)} projects found !`);

    let projectData = await scrapper.getProjectsData(projectLinks)
    displayProjectInfo(projectData)

    console.log("\n---Project Sheets---\n")
    let partition = prompt("No. of sheets : ")
    displaySheets(partition, projectData)

    console.log("\n---END---\n")
}

// entry function
init()
