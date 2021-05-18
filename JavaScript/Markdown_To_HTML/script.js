const marked = require("marked")
const fs = require("fs")

console.log("Reading from file markdown.md...")
fs.readFile("markdown.md", "utf-8", (err, data) => {
    if(err) {
        console.error(err)
        return
    }
    console.log("Writing into file html.html...")
    fs.writeFile("html.html", marked(data, { sanitiser: true }), err => {
        if(err) {
            console.error(err)
            return
        } else {
            console.log("Output generated in file html.html!")
        }
    })
})
