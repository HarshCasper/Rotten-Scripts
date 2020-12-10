const cheerio = require('cheerio');
const got = require('got');
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

readline.question('Provide the URL of the Amazon Prdouct you want to scrape. \n', url => {
    got(url).then(response => {
        const $ = cheerio.load(response.body);
        // Load the reviews
        const reviews = $('.review');
        reviews.each((i, review) => {
            const textReview = $(review).find('.review-text').text();
            console.log(textReview);
        })
    })
    readline.close();
});