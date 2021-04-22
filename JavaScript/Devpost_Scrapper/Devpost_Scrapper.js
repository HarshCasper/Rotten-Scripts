const prompt = require("prompt-sync")()
const scrapper = require("./scrapper")
const init = () => {
    /*
     * 1.get hackathons link as input
     * 2.get hackathons html page data
     * 3.extract project links from page
     * 4.get project info
     * 5.display project data 
     */
    let hackathonsLink = prompt("Enter DevPost link : ")
    let hackathonsData = scrapper.getHackathonsData(hackathonsLink)

    let hackathonsProjectsURL = `${hackathonsLink} + /project-gallery`
    let projectLinks = scrapper.getProjects(hackathonsProjectsURL)
    let projectData = scrapper.getProjectsData(hackathonsProjectsURL)

    displayProjectInfo(projectData)

}

// entry function
init()
