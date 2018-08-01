var Crypto = require('cryptojs');
var c = require('crypto');
Crypto = Crypto.Crypto;

var KEY = 'qweeqwertyuiopasdfghjklñzxcvbnm';
//var IV = 'asdf ñlk kjh asgdfguas alsdhfioashfioah prueba456ahsfkjashflkñjsaflkjñasdf';
var MODE = new Crypto.mode.CBC(Crypto.pad.ZeroPadding);
var IV = '-.,mnbvcrrwedfgd';





// var caracteres = "abcdefghijkmnpqrtuvwxyzABCDEFGHJKMNPQRTUVWXYZ2346789";
// var IV = "";
// for (i=0; i<32; i++) IV +=caracteres.charAt(Math.floor(Math.random()*caracteres.length)); 
//console.log(IV);

// var IV = 'A1B2C3D4E5F6G7H8A2B3C4D5E6F7G8H9';

var plaintext = 'Av. Las Vías 73, Edif 15';
var input_bytes = Crypto.charenc.UTF8.stringToBytes(plaintext);
var key = Crypto.charenc.UTF8.stringToBytes(KEY);
var options = {iv: Crypto.charenc.UTF8.stringToBytes(IV), asBytes: true, mode: MODE};
var encrypted = Crypto.AES.encrypt(input_bytes, key, options);
var encrypted_hex = Crypto.util.bytesToHex(encrypted);
console.log(encrypted_hex); // this is the value you send over the wire
encrypted_hex = 'HRtNxBixvj3cLmrM6FYiYMJtVQCBIwmi6RSXzQhnROQlfT3cg7E5U/3gCsn5S3rxnLEC0+qC1t2nmkk+2MtaFg==';
output_bytes = Crypto.util.hexToBytes(encrypted_hex);
 output_plaintext_bytes = Crypto.AES.decrypt(output_bytes, key, options);
 output_plaintext = Crypto.charenc.UTF8.bytesToString(output_plaintext_bytes);
 console.log(output_plaintext); // result: 'The answer is no'