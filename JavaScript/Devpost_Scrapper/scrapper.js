const fetch = require("node-fetch")
const parser = require("node-html-parser")

const makeRequest = async (url) => {
    let res = await fetch(url)
    return res.text()
}

const getHackathonsData = async (url) => {
    let data = {}
    let htmlData = await makeRequest(url)
    htmlData = parser.parse(htmlData)

    let title = htmlData.querySelectorAll("h1")[1]
    title = (title) ? title.innerText : "Not Found"

    let description = htmlData.querySelectorAll("h3")[0];
    description = (description) ? description.innerText : "Not Found"

    data = {
        "title": title,
        "description": description
    }
    return data
}
const getProjects = async (url) => {
    let data = {}
    return data
}
const getProjectsData = (arr) => {
    let data = {}
    return data
}
module.exports = { getHackathonsData, getProjects, getProjectsData }
