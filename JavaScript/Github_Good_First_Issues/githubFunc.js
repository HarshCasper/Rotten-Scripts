const fetch = require("node-fetch")
const githubToken = require("./token.js")

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

const getRepoViaJson = () => {

}

const getRepoFromTrending = () => {

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
        return getRepoViaJson()
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
