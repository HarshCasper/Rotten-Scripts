const marked = require("marked")
const fs = require("fs")

console.log("Reading from file markdown.md...")
fs.readFile("markdown.md", "utf-8", (err, data) => {
    if(err) {
        console.error(err)
        return
    }
    console.log("Writing into file index.html...")
    fs.writeFile("index.html", marked(data, { sanitiser: true }), err => {
        if(err) {
            console.error(err)
            return
        } else {
            console.log("Output generated in file index.html!")
        }
    })
})
