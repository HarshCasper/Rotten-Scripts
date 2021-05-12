const puppeteer = require('puppeteer')
const cred = require("./cred")

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
            let timeDelay = 400

            let timer = setInterval(() => {
                let totalHeight = document.body.scrollHeight
                window.scrollBy(0, distance);
                scroll += distance;

                if (totalHeight <= scroll) {
                    clearInterval(timer);
                    resolve()
                }
            }, timeDelay)
        });
    });
}

const getProfilePage = async (url) => {

    let browser = await puppeteer.launch({
        headless: true, args: ['--window-size=1920,1080'],
        defaultViewport: null
    });

    // login page
    let loginURL = "https://www.linkedin.com/login"
    let loginPage = await browser.newPage()
    await loginPage.goto(`${loginURL}`, { waitUntil: 'networkidle0', timeout: 0 })

    // login via credentials
    console.log("\nProgress report :");
    console.log("-Logging in");
    await delay(2000)
    await loginPage.type('#username', cred.email)
    await loginPage.type('#password', cred.password)
    await delay(2000)
    await loginPage.click('.btn__primary--large')
    console.log("-Logged in\n-Moving to the profile");

    // navigate to the profile
    await delay(6000)
    console.log("-loading profile");
    let page = await browser.newPage()
    await page.goto(`${url}`)

    // scrolling and loading
    console.log("-waiting for scroll")
    await delay(6000)
    await autoScroll(page)
    console.log("-Loaded");

    await delay(2000)

    return {
        "page": page,
        "browser": browser
    }
}

const getEndorsements = async (url) => {
    let endorsements = []
    let data = await getProfilePage(url)
    let page = data.page
    let browser = data.browser

    console.log("-Collecting data .. this may take sometime");
    // click more skill button
    await page.evaluate(() => {
        let btn = document.querySelectorAll("button.pv-profile-section__card-action-bar")[0]
        btn.click()
    })

    let allSkills = await page.evaluate(async () => {

        let timeDelay = (time) => {
            return new Promise(function (resolve) {
                setTimeout(resolve, time)
            });
        }

        let autoScrollWindow = async () => {
            await new Promise((resolve, reject) => {
                let scroll = 0
                let distance = 100
                let timeDelay = 500

                let timer = setInterval(() => {
                    let elem = document.querySelectorAll(".artdeco-modal__content")[0]
                    let totalHeight = elem.scrollHeight
                    elem.scrollBy(0, distance);
                    scroll += distance;

                    if (totalHeight <= scroll) {
                        clearInterval(timer);
                        resolve()
                    }
                }, timeDelay)
            });
        }

        let skills = document.querySelectorAll("span.pv-skill-category-entity__name-text")
        if (skills.length == 0) {
            return []
        }
        let closeBtn = document.querySelectorAll(".artdeco-modal__dismiss.artdeco-button")
        let skillArr = []
        for (let i = 0; i < skills.length; i++) {

            let peopleNames = []
            if (skills[i].parentElement.href != undefined) {

                skills[i].click()
                await timeDelay(3000)
                await autoScrollWindow()

                let people = document.querySelectorAll("span.pv-endorsement-entity__name--has-hover")

                for (let i = 0; i < people.length; i++) {
                    peopleNames.push(people[i].innerText)
                }
            }

            let obj = {
                "skill": skills[i].innerText,
                "people": peopleNames,
                "number": peopleNames.length
            }
            skillArr.push(obj)
        }
        return skillArr
    });

    await browser.close()
    endorsements = allSkills
    return endorsements
}

module.exports = { getEndorsements }
