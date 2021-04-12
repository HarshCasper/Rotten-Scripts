//adding req module 
const{PDFDocument} = require('pdf-lib');

//importing file system 
const fs = require('fs');

//to catch any error
run().catch(err  => console.log(err));

async function run(){
    //loading pdf1
    const pdf1 = await PDFDocument.load(fs.readFileSync('./Hello.pdf'));
    
    //loading pdf2
    const pdf2 = await PDFDocument.load(fs.readFileSync('./World.pdf'));
    
    //creating a blank pdf named doc
    const doc = await PDFDocument.create();
    
    //for loop to paste contents of pdf1 to doc
    const pdfPages1 = await doc.copyPages(pdf1, pdf1.getPageIndices());
    for (const page of pdfPages1){
        doc.addPage(page);
    }
    
    //for loop to paste contents of pdf1 to doc
    const pdfPages2 = await doc.copyPages(pdf2, pdf2.getPageIndices());
    for(const page of pdfPages2){
        doc.addPage(page);
    }
    
    //writing the contents from doc to final_merged_pdf
    fs.writeFileSync('./final_merged_pdf.pdf', await doc.save());
}
