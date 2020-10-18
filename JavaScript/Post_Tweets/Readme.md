## Post Tweets

A script to post tweets with media and caption using twit npm package.

`var T = new Twit({..})`

Creates a Twit instance that can be used to make requests to Twitter's APIs.

* Update the keys in the object which are provided in your twitter developer portal.

`T.post(path, [params], callback)`

GET any of the REST API endpoints.

**path**

The endpoint to hit. When specifying path values, omit the '.json' at the end

**params**

(Optional) parameters for the request.

**callback**

function (err, data, response)

data is the parsed data received from Twitter.
response is the http.IncomingMessage received from Twitter.
