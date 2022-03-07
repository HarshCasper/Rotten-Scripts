import fetch from "node-fetch";
import { parse } from 'node-html-parser';
import PDFDocument from "pdfkit";
import fs from 'fs';

console.log("Downloading...");
const dateTime = new Date();
const paperName ="telegraphindia";
const year = `${dateTime.getFullYear()}`;
const month = `${dateTime.getMonth()+1}`;
const date = `${dateTime.getDate()-1}`;
const URL = `https://epaper.${paperName}.com/calcutta/${year}-${month}-${date}/71/Page-1.html`;

const getRawData = async (URL) => {
    const response = await fetch(URL);
    const data = await response.text();
    return data;
};

const gettelegraphindia = async () => {
    const telegraphindia = await getRawData(URL);
    const root = parse(telegraphindia);
    const totalPage = root.querySelector('#totalpages').rawAttributes.value
    const totalDate = `${date.length==2?date:"0"+date}${month.length==2?month:"0"+month}${year}`
    const doc = new PDFDocument({
        size: [419, 673],
    });
    doc.pipe(fs.createWriteStream(`${paperName} ${date}-${month}-${year}.pdf`));
    for(let i=1; i<=totalPage; i++){
        await fetch(`https://epaper.${paperName}.com/epaperimages////${totalDate}////${totalDate}-md-hr-${i}.jpg`, {
            method: 'GET'
        }).then(res => res.buffer().then(buffer => {
            doc.image(buffer, 0, 0, {
                width: 419,
                height: 673
            });
        }));
        if(i<totalPage) {
            doc.addPage({
                size: [419, 673],
            });
        }
    }
    doc.end();
    console.log("Download Finished");
};

gettelegraphindia();