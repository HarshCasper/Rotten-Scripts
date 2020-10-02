const { Octokit } = require("@octokit/core");
const { exit } = require("process");
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
  })
  
const request = require('request')

// Script to generate issues

function generate(octokit, owner, repo, callback) {

        request({url: 'http://www.randomtext.me/api/gibberish/p-1/50-100/', json: true}, (error, {body}) => {
            body = body['text_out']
            // uses the octokit request package for applying a POST request for creating an issue
            octokit.request('POST /repos/{owner}/{repo}/issues', {
                owner: owner,
                repo: repo,
                title: 'Issue',
                body: body
            })
            .then((response) => callback(`Issue Created!`))   // Callback to avoid printing before execution
        })
}

// Takes user input for owner and repo

function input(octokit, callback) {
    readline.question(`\nGitHub Owner: `, owner => {
        readline.question(`\nRepo: `, repo => {
            readline.question(`\nNo of Issues to bomb with: `, no => {
                console.log('\nGenerating issues... press Ctrl+C once done!\n')
                for(let i = 0; i < no; i++) {
                    // Call generate to create issues
                    generate(octokit, owner, repo, msg => {console.log(msg)})
                }
            })

        })
    })



}

function start()
{
readline.question(`\nHey there! To use this feature, generate an access token at https://github.com/settings/tokens/new?scopes=repo \nAccess Token: `, token => {
    const octokit = new Octokit({ auth: `${token}` });    

    // This is a just a test request to check whether the token is correct
    
    octokit.request("GET /orgs/:org", {
        org: "octokit"
    }).then((response) => {
        console.log(`\nYou're in! Enter the GitHub Owner who's repository you choose to bomb:\n`)
        
        // Get Started if the token is correct!
        input(octokit)
    })
    .catch((error) => {console.log('\nBad Credentials!\n'); start();}) 
  })

}

start()


