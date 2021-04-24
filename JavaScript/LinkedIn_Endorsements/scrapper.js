const fetch = require("node-fetch")
const parser = require("node-html-parser")

const makeRequest = async (url) => {
    let res = await fetch(url)
    return res.text()
}

const getEndorsements = async (link) => {
    let endorsements = []

    let htmlData = await makeRequest(link)
    htmlData = parser.parse(htmlData)


    return endorsements
}

module.exports = { getEndorsements }