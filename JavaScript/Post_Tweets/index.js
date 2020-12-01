var Twit = require('twit')
const fs = require('fs');
var T = new Twit({
  consumer_key:         'YOUR_CONSUMER_KEY',
  consumer_secret:      'YOUR_CONSUMER_SECRET',
  access_token:         'YOUR_ACCESS_TOKEN',
  access_token_secret:  'YOUR_ACCESS_SECRET',
})
 
// post tweet 
var text = "ENTER_TWEET_TEXT"
T.post('statuses/update', { status: text }, function(err, data, response) {
  console.log("tweeted", text)
})
 
//
// post a tweet with media
//
var imagePath ='ENTER_IMAGE_PATH'
var caption = 'ENTER_CAPTION'

var b64content = fs.readFileSync(imagePath, { encoding: 'base64' })

T.post('media/upload', { media_data: b64content }, function (err, data, response) {
  var mediaIdStr = data.media_id_string
  var altText = "ENTER_ALT_TEXT"
  var meta_params = { media_id: mediaIdStr, alt_text: { text: altText } }
 
  T.post('media/metadata/create', meta_params, function (err, data, response) {
    if (!err) {
      var params = { status: caption, media_ids: [mediaIdStr] }
 
      T.post('statuses/update', params, function (err, data, response) {
        console.log("tweeted image with caption")
      })
    }
  })
})
