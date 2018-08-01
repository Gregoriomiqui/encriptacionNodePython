# -*- coding: utf-8 -*-
from Crypto.Hash import SHA256
import hashlib
from Crypto.Cipher import AES
import base64
import os, sys
from os import urandom

KEY = '65910B1141CA4D186690392F322D5F69'

def encrypt(key, plaintext):

    sha256 = SHA256.new()
    sha256.update(key)
    
    iv = urandom(16)

    aes = AES.new(os.urandom(32), AES.MODE_CTR, counter = lambda : os.urandom(16))

    plaintext = hashlib.sha256(bytearray.fromhex(plaintext)).hexdigest()
    ciphertext = aes.encrypt(plaintext)
    return ciphertext
   # var encrypted = Buffer.concat([iv, ciphertext, cipher.final()]).toString('base64');

    #return encrypted;
a = encrypt(KEY,"soy una canción")
print a