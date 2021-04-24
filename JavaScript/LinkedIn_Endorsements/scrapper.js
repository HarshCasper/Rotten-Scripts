const puppeteer = require('puppeteer')
const parser = require("node-html-parser")

const makeRequest = async (url) => {
    let res = await fetch(url)
    return res.text()
}

const getEndorsements = async (url) => {
    let endorsements = []

    let browser = await puppeteer.launch({ headless: false });

    let loginURL = "https://www.linkedin.com/login";
    let loginPage = await browser.newPage();
    await page.goto(`${loginURL}`, { waitUntil: 'networkidle0', timeout: 0 });

    await browser.close();

    return endorsements
}

module.exports = { getEndorsements }