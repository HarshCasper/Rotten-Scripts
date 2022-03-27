const covid19 = require('covid19-stats');
const prompt = require('prompt-sync')();
async function main() {
    const country = prompt('Enter the name of the country you need Covid statistics of: ');
    console.log("Details: ");
    let stats = await covid19.getCountry(country);
    console.log(stats);  
}
module.exports.main = main
main();
