const https = require('https')
var fs = require('fs');
var colors=require("colors/safe")

var requestUrl=(host,path)=>{
//Http Request with host and path
    return new Promise((resolve, reject)=>{
        const req = https.request({hostname: host, path: path, method: 'GET'}, res => {
            resolve(res.statusCode);
          });
        req.on('error',(err)=>{
            reject(err);
        });  
        req.end(); 
    });
    
}


async function scanlinks(){
    fs.readFile('paths.txt', 'utf8', async function(err, data) {//getting Links from paths.txt file in current directory 
        if (err) throw err;
        var arr=data.split("\r\n");
        for(var i=0;i<arr.length;i++){
            try{
                var status=await requestUrl(host,arr[i])
                if(status==200)
                    console.log(colors.green(status)+": Admin Panel Found at link "+colors.green(arr[i]));

                else if(status==301 || status==302)
                    console.log(colors.yellow("- "+status)+": Redirected Potential Path"+colors.yellow(arr[i]));

                else
                    console.log(colors.red("X "+status)+": Not Found "+colors.red(arr[i]));
            }
            catch(err){
                if(err.code=="ENOTFOUND"){
                    console.log(colors.red("Error: "+"Wrong Host Provided or 'https://' included (Check your host or Try removing https://)"));
                    break;
                }
                else{
                    console.log(colors.red("Error: "+err.info));
                }
                
            }
            
        }
    });

}

/*
*****************************MAIN FUNCTION******************************************************
 */
var host=process.argv[2];
if(host!==undefined){
    scanlinks();
}

else{
    console.log(colors.red("Error: Please Provide Host Name(Do Not Add https://)"))
}