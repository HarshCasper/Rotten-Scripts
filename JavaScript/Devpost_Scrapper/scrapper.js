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
    let data = []
    let htmlData = await makeRequest(url)
    htmlData = parser.parse(htmlData)

    let projectGallery = htmlData.querySelector("#submission-gallery")
    if (!projectGallery) {
        return []
    }

    let links = projectGallery.querySelectorAll("a")
    if (!links) {
        return []
    }
    data = links.map(link => link.getAttribute("href"))


    return data
}

const getProjectsData = async (arr) => {
    let res = []
    for (let i = 0; i < arr.length; i++) {
        let link = arr[i]
        let htmlData = await makeRequest(link)
        htmlData = parser.parse(htmlData)

        let title = htmlData.querySelector("#app-title")
        title = (title) ? title.innerText : "Not Found"

        let desc = htmlData.querySelectorAll(".large")[1]
        desc = (desc) ? desc.innerText.replace("\n", "").trim() : "Not Found"

        let appDetail = htmlData.querySelector("#app-details-left")
        let subtitle = "Not Found", techUsed = [], images = [];
        if (appDetail) {
            subtitle = appDetail.querySelectorAll("p")[0]
            subtitle = (subtitle) ? subtitle.innerText.replace("\n", "").trim() : "Not Found"
            if (subtitle.length == 0) {
                subtitle = appDetail.querySelectorAll("p")[1]
                subtitle = (subtitle) ? subtitle.innerText.replace("\n", "").trim() : "Not Found"
            }

            let builtWith = appDetail.querySelector("#built-with")
            if (builtWith) {
                techUsed = builtWith.querySelectorAll("a")
                techUsed = (techUsed) ? techUsed.map(a => a.innerText) : "Not Found"
            } else {
                techUsed = []
            }

            images = appDetail.querySelectorAll("img")
            if (images) {
                images = images.map(img => "https:" + img.getAttribute("src"))
            } else {
                images = []
            }
        }

        data = {
            "title": title,
            "description": desc,
            "subtitle": subtitle,
            "images": images,
            "techUsed": techUsed,
            "link": link
        }
        res.push(data)

    }
    return res
}
module.exports = { getHackathonsData, getProjects, getProjectsData }
