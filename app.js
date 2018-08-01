    
    var aes256 = require("aes256");
    var express = require("express");

    

   
    
    
    

    var key = 'qweeqwertyuiopasdfghjklñzxcvbnm';
    var plaintext = "Epale soy el mensaje a encrytar";

    var app= express();

    app.get("/",function(req,res){
        var cipher = aes256.createCipher(key);

        var encrypted = aes256.encrypt(key,plaintext);
        var decryted = aes256.decrypt(key, encrypted);

        let date= new Date();

        console.log("..................... "+date+" ..................................");
        console.log("...................de forma normal....................................");
        console.log("encrypted: "+encrypted);
        console.log("decrypted: "+decryted);

        
        // var encrypted = cipher.encrypt(plaintext);
        // var decryted = cipher.decrypt(encrypted);
        // console.log("............................forma cipher..................................");
        // console.log("encrypted: "+encrypted);
        // console.log("decrypted: "+decryted);

        // let a = cipher.decrypt("otFKSJTA+oUvkVFkRH54lfHbzXlTKUV8opozOx2AZkHMQXke+OHSoSBqY5xSev8=");
        // console.log(a);

        res.end();
        
    });

    app.listen(8080);