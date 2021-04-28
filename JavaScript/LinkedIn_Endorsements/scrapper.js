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
            var totalHeight = 0
            var distance = 100
            var timer = setInterval(() => {
                var scrollHeight = document.body.scrollHeight;
                page.scrollBy(0, distance)
                totalHeight += distance

                if (totalHeight >= scrollHeight) {
                    clearInterval(timer)
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
    await delay(2000)
    await loginPage.type('#username', cred.email)
    await loginPage.type('#password', cred.password)
    await delay(2000)
    await loginPage.click('.btn__primary--large')

    // navigate to the profile
    await delay(6000)
    let page = await browser.newPage()
    await page.goto(`${url}`, { waitUntil: 'networkidle0', timeout: 0 })
    await page.hover("#ember480");

    // await browser.close();

    return endorsements
}

module.exports = { getEndorsements }