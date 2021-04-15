/*adding req PDFDocument module of pdf-lib and file systems lib,
need to be downloaded in json package before implementing the code*/

const {PDFDocument} = require('pdf-lib');
const file_sys = require('fs');


// to catch and log errors
main_fun().catch(errors => console.log(errors));


//async main_fun is declared
async function main_fun(){

    // an empty pdf is created using create() function of file systems
    const empty_pdf = await PDFDocument.create();


    /*adding first pdf using readFileSync function of file systems
    await is used to make it wait while pdf1 is loading*/

    const pdf1 = await PDFDocument.load(file_sys.readFileSync('./Hello.pdf'));


     /*adding second pdf
    await is used to make it wait while pdf2 is loading*/
    
    const pdf2 = await PDFDocument.load(file_sys.readFileSync('./World.pdf'));
    

    /* pages of pdf1 are copied to empty pdf 
    
    getPagesIndices() function of file systems is used to get number of pages in pdf1   
    to use it as range in for loop while traversing*/
    const page_pdf1 = await empty_pdf.copyPages(pdf1, pdf1.getPageIndices());



    //for loop is used to traverse pdf within its index to add pages to empty_pdf
    for (const page of page_pdf1)
    {

        //pages added using addPge() fun of file systems
        empty_pdf.addPage(page);
    }


/* pages of pdf2 are copied to empty pdf 
    
    getPagesIndices() function of file systems is used to get number of pages in pdf2
    to use it as range in for loop while traversing*/

    const page_pdf2 = await empty_pdf.copyPages(pdf2, pdf2.getPageIndices());

    
    //for loop is used to traverse pdf within its index to add pages to empty_pdf
    for(const page of page_pdf2){

         //pages added using addPge() fun of file systems
        empty_pdf.addPage(page);
    }

    
    /*using writerFileSync(), function of file sys 
    contents of empty_pdf are wtitten over final_merged_pdf

    save(): to save the pdf, final pdf will appear but won't process otherwise*/

    file_sys.writeFileSync('./final_merged_pdf.pdf', await empty_pdf.save());

}

