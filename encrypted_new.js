var CryptoJS = require('crypto-js');

var key = 'mysecretkey';
var plaintext = 'secret text';

var encrypted_b64 = CryptoJS.AES.encrypt(plaintext, key, key);
console.log("encrypted_text (base64) = "+encrypted_b64);

//output_plaintext = CryptoJS.AES.decrypt(encrypted_b64, key);
var bytes = CryptoJS.AES.decrypt("U2FsdGVkX1+9Wl/biuWHpFKFWo1af8aF14CW/zJjw8c=", key,key);
var output_plaintext = bytes.toString(CryptoJS.enc.Utf8);

console.log("decrypted text = "+output_plaintext);