// program to get the dimensions of an image

const img = new Image();

img.src = '//files/abc.png';

img.onload = function() {
  console.log('width ' + this.width)
  console.log('height '+ this.height);
}
