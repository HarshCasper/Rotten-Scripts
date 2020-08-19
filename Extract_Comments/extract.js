var fs=require('fs');
var extract = require('extract-comments');//Library to Extract Comments from source code
const colors = require('colors/safe');
const { argv } = require('process');
const { Console } = require('console');


if(process.argv[2]!==undefined){
//Reading File    
    console.log(colors.green("Reading File..."));
    fs.readFile(process.argv[2],(err,data)=>{
        if(err){
            console.log(colors.red("Error: Unable To Process File"));
        }
        else{
    
            console.log(colors.green("File Read Successfully!"));
            var sc=data.toString();
            console.log(colors.green("Extracting Comments..."));
            var comments=extract(sc);//Extracting Comments
            console.log(colors.green("Comments Extracted Successfully!"));
            var str="";
            for(var i=0;i<comments.length;i++){
                console.log(colors.green("Writing To File :")+"### "+comments[i].value);    
                str+="### "+comments[i].value+"\n";
            }

            fs.writeFile('./output.md', str, err => {
                if (err) {
                  console.log(colors.red("Something Went Wrong, ERROR"+ err))
                  return
                }
                console.log(colors.yellow("All Comments Written Successfully to file 'output.md' "));
              })
        }
    
    });
}

else{
    console.log(colors.red("Error: Please Provide File Path"));
}





