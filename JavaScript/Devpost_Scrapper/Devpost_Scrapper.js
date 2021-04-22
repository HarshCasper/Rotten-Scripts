const prompt = require("prompt-sync")()
const scrapper = require("./scrapper")

const displayHackathonsInfo = () => {

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
    let hackathonsLink = prompt("Enter DevPost link : ")
    let hackathonsData = await scrapper.getHackathonsData(hackathonsLink)
    displayHackathonsInfo(hackathonsData)

    let hackathonsProjectsURL = `${hackathonsLink} + /project-gallery`
    let projectLinks = await scrapper.getProjects(hackathonsProjectsURL)
    let projectData = await scrapper.getProjectsData(projectLinks)

    displayProjectInfo(projectData)
}

// entry function
init()
