const puppeteer = require('puppeteer')
const cred = require("./cred")
const parser = require("node-html-parser")

const delay = (time) => {
    return new Promise(function (resolve) {
        setTimeout(resolve, time)
    });
}

const autoScroll = async (page) => {
    await page.evaluate(async () => {
        await new Promise((resolve, reject) => {
            let scroll = 0
            let distance = 100

            let timer = setInterval(() => {
                let totalHeight = document.body.scrollHeight
                window.scrollBy(0, distance);
                scroll += distance;

                if (totalHeight <= scroll) {
                    clearInterval(timer);
                    resolve()
                }
            }, 400)
        });
    });
}

const getEndorsements = async (url) => {
    let endorsements = []

    let browser = await puppeteer.launch({
        headless: false, args: ['--window-size=1920,1080'],
        defaultViewport: null
    });

    // login page
    let loginURL = "https://www.linkedin.com/login"
    let loginPage = await browser.newPage()
    await loginPage.goto(`${loginURL}`, { waitUntil: 'networkidle0', timeout: 0 })

    // login via credentials
    console.log("Logging in...\n");
    await delay(2000)
    await loginPage.type('#username', cred.email)
    await loginPage.type('#password', cred.password)
    await delay(2000)
    await loginPage.click('.btn__primary--large')
    console.log("Logged in..and..\nMoving to profile\n");

    // navigate to the profile
    await delay(6000)
    console.log("profile is loading");
    let page = await browser.newPage()
    await page.goto(`${url}`)

    console.log("waiting for scroll\n")
    await delay(6000)
    await autoScroll(page)
    // await browser.close();

    return endorsements
}

module.exports = { getEndorsements }