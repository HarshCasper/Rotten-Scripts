var forge = require('node-forge'); //using forge library of javascript
var pki = forge.pki;
var rsa = forge.pki.rsa;//importing RSA 

function getRsaKeys(){
  var keypair = rsa.generateKeyPair({bits: 2048, e: 0x10001});//generating public and private key's
  var pubKeyPEM = pki.publicKeyToPem(keypair.publicKey);
  var privKeyPEM = pki.privateKeyToPem(keypair.privateKey);

  //converting into JSON Object
  var keys={publicKey:pubKeyPEM,privateKey:privKeyPEM};
  //Keys are stored into keys json object
  return keys;
}

console.log(getRsaKeys());

module.exports=(getRsaKeys);