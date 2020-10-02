const { Octokit } = require("@octokit/core");
const { exit } = require("process");
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
  })
  
const request = require('request')

function generate(octokit, owner, repo, callback) {

        request({url: 'http://www.randomtext.me/api/gibberish/p-1/50-100/', json: true}, (error, {body}) => {
            body = body['text_out']
            octokit.request('POST /repos/{owner}/{repo}/issues', {
                owner: owner,
                repo: repo,
                title: 'Issue',
                body: body
            })
            .then((response) => callback(`Issue Created!`))    
        })
}

function input(octokit, callback) {
    readline.question(`\nGitHub Owner: `, owner => {
        readline.question(`\nRepo: `, repo => {
            readline.question(`\nNo of Issues to bomb with: `, no => {
                console.log('\nGenerating issues... press Ctrl+C once done!\n')
                for(let i = 0; i < no; i++) {
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
    octokit.request("GET /orgs/:org", {
        org: "octokit"
    }).then((response) => {
        console.log(`\nYou're in! Enter the GitHub Owner who's repository you choose to bomb:\n`)
        input(octokit)
    })
    .catch((error) => {console.log('\nBad Credentials!\n'); start();}) 
  })

}

start()


