const { PDFDocument }= require('pdf-lib');
const fs= require('fs');


//For catching errors
run().catch(err=>console.log(err));


async function run(){
    //Loading the pdf which we need to convert
    const pdf1 = await PDFDocument.load(fs.readFileSync('1.pdf'));
    const pdf2 = await PDFDocument.load(fs.readFileSync('2.pdf'));

    //creating a new empty document
    const doc = await PDFDocument.create();

    //Adding first pdf to the empty doc
    const first = await doc.copyPages(pdf1, pdf1.getPageIndices());
    for (const page of first){
        doc.addPage(page);
    }

    //Adding second pdf to the empty doc
    const second = await doc.copyPages(pdf2, pdf2.getPageIndices());
    for (const page of second){
        doc.addPage(page);
    }

    //creating a name for merged pdf
    fs.writeFileSync('./rottenscript.pdf',await doc.save());

}
