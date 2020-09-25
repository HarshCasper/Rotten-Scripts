// import turndown module
const TurndownService = require('turndown');
const turndownService = new TurndownService();

// user input
const fs = require('fs');
const path = require('path');
const filepath = windows.prompt("Enter the path of file:");
const file = path.basename(filepath);
  
// Reading data 
fs.readFileSync(file, function(err, data){ 
    if (err) throw err; 
  
    // convert HTML to Markdown
    const markdown = turndownService.turndown(data);
    // Wrtiting it in markdown.md
    fs.writeFileSync('Markdown.md', markdown, function(err) {
        if (err) {
           return console.error(err);
        }
    })    
}) 
