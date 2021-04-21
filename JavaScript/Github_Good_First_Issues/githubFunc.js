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

module.exports = { getRepoViaMethod }
