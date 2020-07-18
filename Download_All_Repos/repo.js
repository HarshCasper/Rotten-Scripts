const shell = require('shelljs');//To clone repos, shell commands
var fs = require('fs');
const https = require('https');
var parse = require('parse-link-header');//To parse link in header
const { Agent } = require('http');

//Setting up max events listeners
const EventEmitter = require('events');
const emitter = new EventEmitter();
emitter.setMaxListeners(200);

/*
* ------------------------------------------------Functions----------------------------------------------------------------------------
*/
//Function to remove already present directory
rmDir = function(dirPath) {
  try { var files = fs.readdirSync(dirPath); }
  catch(e) { return; }
  if (files.length > 0)
    for (var i = 0; i < files.length; i++) {
      var filePath = dirPath + '/' + files[i];
      if (fs.statSync(filePath).isFile())
        fs.unlinkSync(filePath);
      else
        rmDir(filePath);
    }
  fs.rmdirSync(dirPath);
};

//Function to clone a Repository using shelljs
function clone(url){
  
      if(shell.exec('git clone '+ url)==0)
        console.log("Successfully Clonned "+url);
      else
         console.log("ERROR! Clonning "+url);
      
}

//Making Directory to store all cloned Repositories
var makeDirectory=(username)=>{
  var dir = './Repositories_'+username;

  if (!fs.existsSync(dir)){
      console.log("Creating Directory "+dir)
      fs.mkdirSync(dir);
  }
  else
  {
    console.log("Found Exsisting Directory "+dir+" Refreshing..")
    rmDir(dir);
    fs.mkdirSync(dir);
  }
  const path = dir;
  shell.cd(path)
}

//Get all user Repositories and clone 
var getRepos=(apiUrl)=>{

  console.log("Getting Repo links from "+apiUrl);
  const options = {
    host: 'api.github.com',
    path: apiUrl ,
    headers: { 'User-Agent': 'Repo_script' }
  };
  
  https.get(options, function(res) {
    var link=parse(res.headers.link);
    if(link.next){
      getRepos(link.next.url.split('.com')[1]);
    }
    var body='';
    res.on('data', function(chunk) {
      body+=chunk;
    });
    res.on('end',()=>{
    var data=JSON.parse(body);
    for(var i=0;i<data.length;i++){
      clone(data[i].clone_url);//clone repo Function called
    }
    })
    res.on('error',()=>console.log());
  });

}

/*
* ------------------------------------------------Functions-End----------------------------------------------------------------------------
*/
if(process.argv[2]){
  makeDirectory(process.argv[2]);
  getRepos('/users/'+process.argv[2]+'/repos');
}
else{
  console.log("Error! Github Username Not Provided! Write 'node repo [Your github username]'");
}

