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

const getUsers = async (user, repo) => {
    let users = [], list = [], pageNO = 1;
    while ((list.length > 0 || pageNO == 1) && pageNO < 10) {
        list = await makeRequest(`https://api.github.com/repos/${user}/${repo}/stargazers?per_page=100&page=${pageNO}`)

        // if an array is not returned
        if (list.message) {
            return list
        }
        users = [...users, ...list];
        pageNO++;
    }
    return users;
}

const getUserData = async (username) => {
    let data = await makeRequest(`https://api.github.com/users/${username}`)
    return await data
}
module.exports = { getUsers, getUserData };
