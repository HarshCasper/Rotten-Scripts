const fetch = require("node-fetch")
const githubToken = require("./token.js")
const parser = require("node-html-parser")
const db = require("./DB")

const makeRequest = async (url) => {
    let res = await fetch(url,
        {
            headers: {
                authorization: `token ${githubToken.token}`
            }
        }
    )
    return res.json()
}

const fetchHtml = async () => {
    let res = await fetch("https://github.com/trending")
    let body = await res.text()
    return body
}

const getRepoFromTrending = async () => {
    let htmlData = await fetchHtml()
    htmlData = parser.parse(htmlData);

    let repoList = []
    let articles = htmlData.querySelectorAll("article")
    articles.forEach(element => {

        let h1 = element.querySelectorAll("h1")[0]
        let a = h1.querySelectorAll("a")[0]

        let repoStr = a.innerText.trim();
        repoStr = repoStr.split("/")

        let owner = repoStr[0].trim()
        let name = repoStr[1].replace("\n", "").trim()
        let data = {
            "owner": owner,
            "name": name,
            "url": `https://github.com/${owner}/${name}`
        }
        repoList.push(data)

    });

    return repoList
}

const getRepoFromStarred = async (username) => {
    let repoList = await makeRequest(`https://api.github.com/users/${username}/starred`)
    repoList = repoList.map(elem => {
        return {
            "owner": elem["owner"]["login"],
            "name": elem["name"],
            "url": elem["svn_url"]
        }
    })
    return await repoList
}

const getRepoViaMethod = async (method, username) => {
    method = Number(method)
    if (method == 1) {
        return db
    } else if (method == 2) {
        return getRepoFromTrending()
    } else if (method == 3) {
        return await getRepoFromStarred(username)
    }
    return []
}

const getIssues = async (arr) => {
    let list = []
    for (let i = 0; i < arr.length; i++) {

        let url = `https://api.github.com/repos/${arr[i]["owner"]}/${arr[i]["name"]}/issues?labels=good first issue`

        let issues = await makeRequest(url)
        issues = issues.map(issue => {
            return {
                "title": issue["title"],
                "url": issue["html_url"]
            }
        })

        let data = {
            "repoOwner": arr[i]["owner"],
            "repoName": arr[i]["name"],
            "issues": issues
        }
        list.push(data)
    }
    return list
}

module.exports = { getRepoViaMethod, getIssues }
