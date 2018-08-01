
var CryptoJS = require("crypto-js");
var crypto = require('crypto');

var Crypto = require('cryptojs');
Crypto = Crypto.Crypto;
var CIPHER_ALGORITHM = 'aes-256-cbc';

const utf8 = require('utf8');

encodeUTF8 = (text) =>{
    var outputStr = "";
	

	if (text !== "") {
		var decodedStr = unescape(encodeURIComponent(text));

		for (var pos = 0; pos < decodedStr.length; pos++) {
			outputStr = outputStr.concat("&#");
			outputStr = outputStr.concat(decodedStr.charCodeAt(pos));
			outputStr = outputStr.concat(";");
		}
    }
    return outputStr;

}



// Encryption using AES CBC (128-bits)
encrypt = (plaintext, passphrase) => {
    try {
    
    //passphrase =  CryptoJS.enc.Utf8.parse(passphrase);
     
     var sha256 = crypto.createHash('sha256');
     sha256.update(passphrase);
     console.log(sha256);
    
     plaintext = Crypto.charenc.UTF8.stringToBytes(plaintext);
     console.log(plaintext);
        

    //  plaintext = Crypto.charenc.UTF8.stringToBytes(passphrase);

    //  console.log(plaintext);

     var iv = crypto.randomBytes(16);
     
     var cipher = crypto.createCipheriv(CIPHER_ALGORITHM, sha256.digest(), iv);
     cipher.setAutoPadding(true);
     var ciphertext = cipher.update(new Buffer(plaintext));
     var encrypted = Buffer.concat([iv, ciphertext, cipher.final()]).toString('base64');
     console.log(encrypted);

     return encrypted;

    //  var encrypted = CryptoJS.AES.encrypt(
    //     plaintext,
    //     sha256.digest(),
    //     { 
    //       mode: CryptoJS.mode.CBC, 
    //       iv: iv, 
    //       // PKCS#7 with 8-byte block size
    //       padding: CryptoJS.pad.Pkcs7 
    //     }
    //   );
    //   return encrypted.ciphertext.toString(CryptoJS.enc.Base64);
    } catch (error) {
      console.log('Encryption exception in encrypt(): ' + error.message);
    }
}

// encripted2 =() => {

// var plaintext = 'Canción';
// var key = "español";

// var iv = crypto.randomBytes(16);
// key = key.toString(CryptoJS.enc.Utf8);
// var sha256 = crypto.createHash('sha256');
// sha256.update(new Buffer(key));


// plaintext = plaintext.toString(CryptoJS.enc.Base64);
// plaintext = CryptoJS.enc.Utf8.parse(plaintext);
// console.log(plaintext);
// console.log(key);

// // var encrypted = CryptoJS.AES.encrypt(
// //         plaintext,
// //         sha256.digest(),
// //         { 
// //           mode: CryptoJS.mode.CBC, 
// //           iv: iv, 
// //           // PKCS#7 with 8-byte block size
// //           padding: CryptoJS.pad.Pkcs7 
// //         }
// //       );
// //       return encrypted.ciphertext.toString(CryptoJS.enc.Base64);



// }

encrypt("hola","casa");



// let a = encrypt("Canción", "español");
// console.log(a);

