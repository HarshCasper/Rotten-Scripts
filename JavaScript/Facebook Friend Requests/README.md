# js Script to accept all friend requests

## What is this?

GThe script, once runs (instructions below), works in the background on the page and keeps on accepting friend requests on the page as long as either it meets maximum requests specified by you or there are no more friend requests. The script has an adequate amount of delay placed between actions so you are not banned 

## How to use the above script?

- Open Facebook, log in, and go to https://www.facebook.com/friends/requests/.
- Please open the developer console of your browser following the instructions here for your browser.
- Copy the entire above script and paste it in the console and hit enter.
- Do not close or refresh the browser tab unless you want the script to stop abruptly.

## When does the script stop gracefully?

- When there are no requests to accept.
- When the number of max requests (if specified) is reached.


## What to configure?

If it is taking too long or you are on a very fast internet connection, you can lower the delays between each action since elements will be loading faster for you. Below is an explanation of what each of the configuration item does:

- scrollDelay: specifies the wait in milliseconds after scrolling page to the bottom to load more friend requests.
- actionDelay: specifies the delay in milliseconds between each click of the confirm button.
- maxRequestsToAccept: set to a positive number to limit the number of friend requests to be accepted to that numbers; a negative number leads to infinite friend requests being accepted (not really).
- totalRequestsAccepted: stores the number of total requests accepted (displayed when the script stops gracefully) and is not to be changed and should remain 0.

## Acknowledgement

This script takes inspiration from the LinkedIn AutoConnect script (https://gist.github.com/thealphadollar/23490d05d1b0c695ea15c5cf23732aca)
