/*
This script is capable of converting some special/secret text 
into 64 BASE Encoded String which is really difficult to decode without a decoder.
This way our data is secured.
*/

/*
------This Script works only on the console/terminal of any browser as node is unknown to the JavaScript functions used here.------
*/

//  ENCODING 

// Here, myStr is my secret String which i want to Encode
let myStr = 'Rotten Scripts are awesome!!';

// encodedStr contains the value of Encoded String of our myStr
let encodedStr = btoa(myStr);

// Printing encodedStr
console.log(encodedStr);        // Um90dGVuIFNjcmlwdHMgYXJlIGF3ZXNvbWUhIQ==


// DECODING

// Here we have some other 64 Base Encoded String, we try to decode it
let encodedStr2 = 'SSBsb3ZlIEphdmFTY3JpcHQ=';

// decodedStr contains the value of Decoded String of our encodedStr2
let decodedStr = atob(encodedStr2);

// Printing decodedStr
console.log(decodedStr);        // I love JavaScript
