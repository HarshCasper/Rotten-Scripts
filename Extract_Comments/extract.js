var fs=require('fs');
var extract = require('extract-comments');
const colors = require('colors/safe');
const { argv } = require('process');
const { Console } = require('console');
if(process.argv[2]!==undefined){
    fs.readFile(process.argv[2],(err,data)=>{
        if(err){
            console.log(colors.red("Error: ")+"Unable To Process File");
        }
        else{
    
            var sc=data.toString();
            var comments=extract(sc);
            for(var i=0;i<comments.length;i++){
                console.log(colors.green(comments[i].type)+": "+comments[i].value);    
            }
        }
    
    });
}

else{
    console.log(colors.red("Error: ")+"Please Provide File Path");
}




// pass a string of JavaScript

// extracts comments from a source file
// var commentList = commentExtractor.extractCommentsFromFile('extract.js');
//  console.log(commentList);
// extracts comments from a source code
//var commentList = commentExtractor.extractCommentsFromString('source code', {language: ''});
 
// extracts TODOs contained in comments
//var todoList = commentExtractor.extractTodosFromComments(commentList);
