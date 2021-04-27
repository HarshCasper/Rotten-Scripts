const fs = require('fs')
const read = (fileName) => {
    if (!fs.existsSync(fileName)) {
        write(fileName, {});
        return "{}";
    }
    return fs.readFileSync(fileName, 'utf-8', (err, data) => {
        if (err) {
            throw err;
        }

        return data;
    });
}
const write = (fileName, data) => {
    fs.writeFile(fileName, JSON.stringify(data), (err) => {
        if (err) {
            throw err;
        }
    });
}

module.exports = { read, write }
