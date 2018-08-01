var CryptoJS = require("crypto-js");

var IV = '-.,mnbvcrrwedfgd';
var KEY = 'qweeqwertyuiopasdfghjklñzxcvbnm';

// Encryption using AES CBC (128-bits)
encrypt = (plaintext, passphrase, iv) => {
    try {
      var encrypted = CryptoJS.AES.encrypt(
        plaintext,
        CryptoJS.enc.Utf8.parse(passphrase),
        { 
          mode: CryptoJS.mode.CBC, 
          iv: CryptoJS.enc.Utf8.parse(iv), 
          // PKCS#7 with 8-byte block size
          padding: CryptoJS.pad.Pkcs7 
        }
      );
      return encrypted.ciphertext.toString(CryptoJS.enc.Base64);
    } catch (error) {
      console.log('Encryption exception in encrypt(): ' + error.message);
    }
}
    
    // Decryption using AES CBC (128-bits)
decrypt = (ciphertext, passphrase, iv) => {
    try {
      var decrypted = CryptoJS.AES.decrypt(
        ciphertext,
        CryptoJS.enc.Utf8.parse(passphrase),
        { 
          mode: CryptoJS.mode.CBC, 
          iv: CryptoJS.enc.Utf8.parse(iv), 
          // PKCS#7 with 8-byte block size
          padding: CryptoJS.pad.Pkcs7 
        }
      );
      return decrypted.toString(CryptoJS.enc.Utf8);
    } catch (error) {
      console.log('Encryption exception in decrypt(): ' + error.message);
    }
}

var text = "Dios subió a su trono";
var text_encriptado = encrypt(text,KEY,IV);
console.log(text_encriptado);
text_encriptado = 'GH5g1iPthhXLcRuW';
var text_desencriptado = decrypt(text_encriptado,KEY,IV);
console.log(text_desencriptado);