/*adding req PDFDocument module of pdf-lib and file systems lib,
need to be downloaded in json package before implementing the code*/

const {PDFDocument} = require('pdf-lib');
const filesys = require('fs');


// to catch and log errors
mainfun().catch(errors => console.log(errors));


//async main_fun is declared
async function mainfun(){

    // an empty pdf is created using create() function of file systems
    const emptypdf = await PDFDocument.create();


    /*adding first pdf using readFileSync function of file systems
    await is used to make it wait while pdf1 is loading*/

    const pdf1 = await PDFDocument.load(filesys.readFileSync('./Hello.pdf'));


     /*adding second pdf
    await is used to make it wait while pdf2 is loading*/
    
    const pdf2 = await PDFDocument.load(filesys.readFileSync('./World.pdf'));
    

    /* pages of pdf1 are copied to empty pdf 
    
    getPagesIndices() function of file systems is used to get number of pages in pdf1   
    to use it as range in for loop while traversing*/
    const pagepdf1 = await emptypdf.copyPages(pdf1, pdf1.getPageIndices());



    //for loop is used to traverse pdf within its index to add pages to emptypdf
    for (const page of pagepdf1)
    {

        //pages added using addPge() fun of file systems
        emptypdf.addPage(page);
    }


/* pages of pdf2 are copied to empty pdf 
    
    getPagesIndices() function of file systems is used to get number of pages in pdf2
    to use it as range in for loop while traversing*/

    const pagepdf2 = await emptypdf.copyPages(pdf2, pdf2.getPageIndices());

    
    //for loop is used to traverse pdf within its index to add pages to emptypdf
    for(const page of pagepdf2){

         //pages added using addPge() fun of file systems
        emptypdf.addPage(page);
    }

    
    /*using writerFileSync(), function of file sys 
    contents of emptypdf are wtitten over finalmergedpdf

    save(): to save the pdf, final pdf will appear but won't process otherwise*/

    filesys.writeFileSync('./finalmergedpdf.pdf', await emptypdf.save());

}

