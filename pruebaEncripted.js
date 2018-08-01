var crypto = require('crypto');
var Crypto = require('cryptojs');
Crypto = Crypto.Crypto;


var KEY = 'qweeqwertyuiopasdfghjklñzxcvbnm';
var IV = '-.,mnbvcrrwedfgd';

encrypt = (key, plaintext) => {
   
    var sha256 = crypto.createHash('sha256');
    sha256.update(KEY);

    // Initialization Vector
    //var iv = crypto.randomBytes(16);
    // iv = '-.,mnbvcrrwedfgd'
    // iv = Crypto.charenc.UTF8.stringToBytes(iv);

    var iv = crypto.randomBytes(16);
    console.log(iv);

    var cipher = crypto.createCipheriv(CIPHER_ALGORITHM, sha256.digest(), iv);

    // var ciphertext = cipher.update(new Buffer(plaintext));
    // var encrypted = Buffer.concat([iv, ciphertext, cipher.final()]).toString('base64');

    // return encrypted;
  }

let encrypted = encrypt(KEY, "esta es una canción");
  