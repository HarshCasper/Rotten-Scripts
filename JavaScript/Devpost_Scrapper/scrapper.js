const fetch = require("node-fetch")
const parser = require("node-html-parser")

const makeRequest = async (url) => {
    let res = await fetch(url)
    return res.json()
}

const getHackathonsData = async (url) => {
    let data = {}
    let htmlData = await makeRequest(url)
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
