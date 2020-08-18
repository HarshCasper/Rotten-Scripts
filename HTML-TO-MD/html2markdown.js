// import turndown module
const TurndownService = require('turndown');
const turndownService = new TurndownService();
// user input
var htmlcode = window.prompt("Enter your code in html: ");


// convert HTML to Markdown
const markdown = turndownService.turndown(htmlcode);

// output Markdown
console.log(markdown);