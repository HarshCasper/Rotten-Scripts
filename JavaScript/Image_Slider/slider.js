
var currentindex = 1
displaySlides(currentindex);  //Displaying the first slide

function setSlides(num){

    displaySlides(currentindex+=num)  //updating which slides to display

}

function displaySlides(num){
    var x;
    var slides = document.getElementsByClassName("Images");
    if (num > slides.length){    //Looping back to first slide 
        currentindex = 1 
    }
    if (num < 1){                 //looping back to last slide
        currentindex = slides.length
    }
    for(x =0 ; x <slides.length ; x++){    //hiding all slides
        slides[x].style.display = "none";

    }

    slides[currentindex - 1].style.display = "block";  //making only one slide visible
}