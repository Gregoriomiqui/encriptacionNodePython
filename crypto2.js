var crypto = require('crypto');
var Crypto = require('cryptojs');
Crypto = Crypto.Crypto;

var IV = '-.,mnbvcrrwedfgd';
var KEY = 'qweeqwertyuiopasdfghjklñzxcvbnm';

var IV = crypto.randomBytes(16);
var sha256KEY = crypto.createHash('sha256');
sha256KEY.update(KEY);

var sha256KEY = crypto.createHash('sha256');
sha256KEY.update(KEY);

var cipher = crypto.createCipheriv('aes-256-cbc', sha256KEY.digest(), IV);
var string = 'esto es una canción';
cipher.update(new Buffer(string));
var enc = cipher.final('base64');
console.log("String: "+string);
console.log("Encriptado: "+enc);

