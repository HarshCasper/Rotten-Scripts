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

        list = list.map(x => x.login)
        // console.log(list);
        users = [...users, ...list];
        pageNO++;
    }
    // console.log("\nUsers are : ");
    // console.log(users);
    console.log(users.length);
    return users.length;
}
getUsers("HarshCasper", "Rotten-scripts")