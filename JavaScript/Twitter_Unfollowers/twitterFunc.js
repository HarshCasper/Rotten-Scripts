const needle = require('needle');
const getUserId = async (username, bearerToken) => {
    let endpointURL = "https://api.twitter.com/2/users/by?usernames="
    const params = {
        usernames: `${username}`,
        "expansions": "pinned_tweet_id"
    }

    // this is the HTTP header that adds bearer token authentication
    const res = await needle('get', endpointURL, params, {
        headers: {
            "User-Agent": "v2UserLookupJS",
            "authorization": `Bearer ${bearerToken}`
        }
    })

    if (res.body) {
        return res.body;
    } else {
        throw new Error('Unsuccessful request')
    }
}
const getFollowers = async (userId, bearerToken) => {
    let url = `https://api.twitter.com/2/users/${userId}/followers`;
    let users = [];
    let params = {
        "max_results": 1000
    }

    const options = {
        headers: {
            "User-Agent": "v2FollowersJS",
            "authorization": `Bearer ${bearerToken}`
        }
    }

    let hasNextPage = true;
    let nextToken = null;

    while (hasNextPage) {
        let resp = await getPage(params, options, nextToken, url);
        if (resp && resp.meta && resp.meta.result_count && resp.meta.result_count > 0) {
            if (resp.data) {
                users.push.apply(users, resp.data);
            }
            if (resp.meta.next_token) {
                nextToken = resp.meta.next_token;
            } else {
                hasNextPage = false;
            }
        } else {
            hasNextPage = false;
        }
    }

    return users
}

const getPage = async (params, options, nextToken, url) => {
    if (nextToken) {
        params.next_token = nextToken;
    }

    try {
        const resp = await needle('get', url, params, options);

        if (resp.statusCode != 200) {
            console.log(`${resp.statusCode} ${resp.statusMessage}:\n${resp.body}`);
            return;
        }
        return resp.body;
    } catch (err) {
        throw new Error(`Request failed: ${err}`);
    }
}
module.exports = { getUserId, getFollowers };
