'use strict';

const puppeteer = require('puppeteer');
const https = require('https');
const fs = require('fs');
const path = require('path');
require('dotenv').config();

let i = 0; // Global Counting variable
const root_folder = 'courses'
const course_name = process.env.LINKEDIN_COURSE;

(async () => {

    // Fixed size. It can "see" all the necessary tabs (Contents, Transcripts, Exercise Files )
    const width = 1600
    const height = 900

    const linkedin_home = 'https://www.linkedin.com/';
    const course_landing_page = `https://www.linkedin.com/learning/${course_name}`;


    console.log(`Launching the browser...`);
    const browser = await puppeteer.launch({
        headless: true,
        args: [
            `--window-size=${ width },${ height }`
        ]
    });
    try {

        const page = await browser.newPage();
        await page.setViewport({
            width,
            height
        });
        // Go to linkedin page and login
        console.log('Login into Linkedin');
        await page.goto(linkedin_home);
        await page.type('#login-email', process.env.LINKEDIN_EMAIL);
        await page.type('#login-password', process.env.LINKEDIN_PASSWORD);
        await Promise.all([
            page.click('#login-submit'),
            page.waitForNavigation()
        ]);
        // Then move to the learning section in the selected course's homepage (linkedin premium needed)
        console.log('Heading to Linkedin Learning Page');
        await page.goto(course_landing_page);
        // FORCED 2 seconds timeout
        await timeout(2000);
        console.log('Looking  for content section');
        // Click on "Content" section
        await page.click('.course-body__info-tab-name.course-body__info-tab-name-content.ember-view');

        let content = await page.evaluate(() => {
            let divs = [...document.querySelectorAll('.toc-item.ember-view')];
            return divs.map((div) => div.href);
        });

        await processData(page, content);

        console.log('Closing...');
        await browser.close();
        console.log('DONE!')
    } catch (e) {
        console.log('Closing...');
        await browser.close();
    }
})();


const processData = (page, content) => new Promise(async (resolve, reject) => {
    try {
        if (!content || content.length === 0) {
            console.log('Did not find any content. There might be two possibilities:\n1 - Your credentials are wrong\n2 - The course\'s name is wrong');
            return resolve();
        }

        let dir = `./${root_folder}`
        if (!fs.existsSync(dir)) {
            console.log(`Creating folder ${root_folder}`);
            fs.mkdirSync(dir);
        }
        dir = `./${root_folder}/${course_name}`
        if (!fs.existsSync(dir)) {
            console.log(`Creating folder ${course_name}`);
            fs.mkdirSync(dir);
        }

        await download_exercise_files(page);
        for (const el of content) {
            await find_uri_and_download(page, el)
        }
        return resolve();
    } catch (e) {
        return reject(e);
    }
});


const find_uri_and_download = (page, content) => new Promise(async (resolve, reject) => {
    try {
        let name = path.basename(content).split('?')[0];
        console.log('Content name: ', name);
        await Promise.all([
            page.goto(content),
            page.waitForNavigation({
                waitUntil: 'domcontentloaded'
            })
        ]);

        let uri = await page.evaluate(() => {
            let src = document.querySelector('.vjs-tech');
            return ((src) ? src.src : null)
        });
        if (!uri) {
            console.log('Skipping content. src not found...');
            return resolve();
        }

        await Promise.all([
            download_uri(uri, name),
            download_transcripts(page, name)
        ]);
        i = i + 1;
        return resolve();
    } catch (err) {
        return reject(err);
    }
});


const download_uri = (uri, name) => new Promise((resolve, reject) => {
    const file = fs.createWriteStream(`./${root_folder}/${course_name}/${i}-${name}.mp4`);
    const request = https.get(uri, function (response) {
        response.pipe(file);
        console.log(`Finished downloading ${name}`);
        return resolve();
    });
});


const download_transcripts = (page, name) => new Promise(async (resolve, reject) => {
    try {
        await page.click('.course-body__info-tab-name.course-body__info-tab-name-transcripts.ember-view');
        let transcript = await page.evaluate(() => {
            let trcps = [...document.querySelectorAll('.transcript')];
            return trcps.map((t) => t.innerText);
        });
        let txt = transcript.join(' ');
        fs.writeFile(`./${root_folder}/${course_name}/${i}-${name}.txt`, txt, function (err) {
            if (err) {
                console.log('An error occurred while looking for transcripts. Skipping...');
                return resolve();
            } else {
                return resolve();
            }
        });
    } catch (err) {
        console.log('An error occurred while looking for transcripts. Skipping...');
        return resolve();
    }
});


const download_exercise_files = page => new Promise(async (resolve, reject) => {
    try {
        await page.click('.course-body__info-tab-name.course-body__info-tab-name-exercise-files.ember-view');
        let files = await page.evaluate(() => {
            let f_ex = [...document.querySelectorAll('.exercise-file-link.exercise-file-unlocked.ember-view')];
            return f_ex.map((f) => f.href);
        });
        if (!files || files.length === 0) {
            console.log('Could not find any exercise file');
            return resolve();
        }
        files.map((f) => {
            let name = path.basename(f).split('?')[0];
            const ex = fs.createWriteStream(`./${root_folder}/${course_name}/${name}`);
            ex.on('error', function (err) {
                console.log(err);
                ex.end();
                return reject(err);
            });
            const request = https.get(f, function (response) {
                response.pipe(ex);
                console.log('Finished downloading exercise files');
                return;
            });
        });
        return resolve();
    } catch (err) {
        console.log('An error occurred while looking for exercises. Skipping...');
        return resolve();
    }
});


const timeout = ms => new Promise(res => setTimeout(res, ms))
