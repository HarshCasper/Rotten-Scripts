const fetch = require("node-fetch")
const parser = require("node-html-parser")

const makeRequest = async (url) => {
    let res = await fetch(url)
    return res.text()
}

module.exports = { getHackathonsData, getProjects, getProjectsData }