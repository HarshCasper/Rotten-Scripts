# linkedin_learning_downloader
Simple script to download videos, transcripts and exercise files from the courses of your choice!


## How it works

You need a Linkedin Premium Account.<br/>
You need to have Node.js installed.<br/>
Download the project.<br/>
Open the terminal in the project folder and type:
```
npm install
```
to download necessary modules. (N.B. Puppeteer is a biiiig module).<br/>
Modifiy the .env file adding your Linkedin username(email) and password.<br/>
In order to properly set the LINKEDIN_COURSE, open the course you are interested in, e.g.:
```
https://www.linkedin.com/learning/node-js-deploying-applications
```
The last part of the url is what we are interested in.
```
node-js-deploying-applications
```
The .env file should look like this:
```
LINKEDIN_EMAIL=your.linkedin@email.com
LINKEDIN_PASSWORD=your_linkedin_password
LINKEDIN_COURSE=node-js-deploying-applications
```
Now, start the .js script to download the course:

```
node ./index.js

```
