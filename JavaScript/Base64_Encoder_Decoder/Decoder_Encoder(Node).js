/*
This script is capable of converting some special/secret text 
into 64 BASE Encoded String which is really difficult to decode without a decoder.
This way our data is secured.
*/

/*
------This Script works fine on command line with Node.------
syntax : node Decoder_Encoder(Node).js
*/

//  ENCODING 

// Here, myStr is my secret String which i want to Encode
let myStr = 'Rotten Scripts are awesome!!';

// Using node, getting text from 'utf-8' and convereting it to 'base64'
// encodedStr contains the value of Encoded String of our myStr
let buff = Buffer.from(myStr, 'utf-8');  
let encodedStr = buff.toString('base64');

// Printing encodedStr
console.log(encodedStr);        // Um90dGVuIFNjcmlwdHMgYXJlIGF3ZXNvbWUhIQ==


// DECODING

// Here we have some other 64 Base Encoded String, we try to decode it
let encodedStr2 = 'SSBsb3ZlIEphdmFTY3JpcHQ=';

// Using node, getting text from 'base64' and convereting it to 'utf-8'
// decodedStr contains the value of Decoded String of our encodedStr2
let buff2 = Buffer.from(encodedStr2, 'base64');  
let decodedStr = buff2.toString('utf-8');

// Printing decodedStr
console.log(decodedStr);        // I love JavaScript
