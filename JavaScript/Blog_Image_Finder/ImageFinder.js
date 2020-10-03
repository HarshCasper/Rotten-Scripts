// All DOM variables
let container = document.querySelector('.container');

// Enter your Unsplash API key here
let key = '';

let btn = document.querySelector('#btn');
let input = document.querySelector('#query');

// function to retrieve photos from unsplash API
async function getPhotos(reqURL){
    let res = await fetch(reqURL);
    let data = await res.json();
    console.log(data);
    if(data.results.length){
        for(let i = 0; i < data.results.length; i++){
            let img = document.createElement('img'); 
            img.src = data.results[i].links.download;
            img.height = "200";
            img.width  = "200";
            container.appendChild(img);
            img.addEventListener('click',()=>{
                alert(img.src);
            })
        }
    }else{
        alert('No images Found for this input!');
    }
}

// init function
function init(){
    let word = input.value;
    input.value = "";
    container.textContent = "";
    let reqURL = `https://api.unsplash.com/search/photos?per_page=30&query=${word}&client_id=${key}`;
    getPhotos(reqURL);
}

// Setting up all event listeners
btn.addEventListener('click', init);
document.addEventListener("keypress",e =>{
    if(e.which === 13)init();
})
