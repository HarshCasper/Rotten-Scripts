var fs=require('fs');
var extract = require('extract-comments');//Library to Extract Comments from source code
const colors = require('colors/safe');
const { argv } = require('process');
const { Console } = require('console');


if(process.argv[2]!==undefined){
//Reading File    
    fs.readFile(process.argv[2],(err,data)=>{
        if(err){
            console.log(colors.red("Error: ")+"Unable To Process File");
        }
        else{
    
            var sc=data.toString();
            var comments=extract(sc);//Extracting Comments
            for(var i=0;i<comments.length;i++){
                console.log(colors.green(comments[i].type)+": "+comments[i].value);    
            }
        }
    
    });
}

else{
    console.log(colors.red("Error: ")+"Please Provide File Path");
}





