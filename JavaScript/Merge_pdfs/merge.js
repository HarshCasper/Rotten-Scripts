const{PDFDocument} = require('pdf-lib');
const fs = require('fs');

run().catch(err  => console.log(err));

async function run(){
    const pdf1 = await PDFDocument.load(fs.readFileSync('./Hello.pdf'));
    const pdf2 = await PDFDocument.load(fs.readFileSync('./World.pdf'));
    const doc = await PDFDocument.create();
    const pdfPages1 = await doc.copyPages(pdf1, pdf1.getPageIndices());
    for (const page of pdfPages1){
        doc.addPage(page);
    }
    const pdfPages2 = await doc.copyPages(pdf2, pdf2.getPageIndices());
    for(const page of pdfPages2){
        doc.addPage(page);
    }
    fs.writeFileSync('./final_merged_pdf.pdf', await doc.save());
}
