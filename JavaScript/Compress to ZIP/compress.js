const zlib = require("zip-lib");
const path = require("path")

//compress single file  

const compressSingleFile = async (sourceFilePath , compressFilePath) =>{

    try {
      await zlib.archiveFile(sourceFilePath,compressFilePath)
      console.log("Successfully compressed the file!");
        
    } catch (error) {
        console.log("Oops! something happened ");
        console.log("Error message" + error.message);
    }
}


//try something like below ----- 
// compressSingleFile("./test.txt","./test-compress.zip")



const compressSingleFolder = async (sourceFolderPath , compressFolderPath) =>{

    try {
      await zlib.archiveFolder(sourceFolderPath,compressFolderPath)
      console.log("Successfully compressed the Folder " + path.basename(sourceFolderPath));
        
    } catch (error) {
        console.log("Oops! something happened ");
        console.log("Error message" + error.message);
    }
}

//try something like below ----- 
//compressSingleFolder("./testfolder","./testfolder-compress.zip")


const compressMultiple = async ({filePaths,folderPaths,compressPath}) =>{

    try {
     
        const zip = new zlib.Zip();
        if(filePaths.length!==0){
            filePaths.forEach(async path=>{
                await zip.addFile(path);
            })
        }

        if(folderPaths.length!==0){
            folderPaths.forEach(async path=>{
                await zip.addFolder(path);
            })
        }

        await zip.archive(compressPath)
        console.log("Successfully compressed as " + path.basename(compressPath));
    } catch (error) {
        console.log("Oops! something happened ");
        console.log("Error message" + error.message);
    }
}


//try something like below ----- 

// compressMultiple({
//     filePaths:["./test.txt"],
//     folderPaths :["./testfolder"],
//     compressPath:"./compressed.zip"
// })


module.exports = {compressSingleFile,compressSingleFolder,compressMultiple}
