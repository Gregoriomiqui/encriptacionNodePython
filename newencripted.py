# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
from Crypto import Random
import pkcs7
import hashlib
import base64

BLOCK_SIZE = 16
key = b"1234567890123456"

def pad(data):
    length = BLOCK_SIZE - (len(data) % BLOCK_SIZE)
    return data + chr(length)*length

def unpad(data):
    return data[:-ord(data[-1])]

def encrypt(message, passphrase):
    key = hashlib.sha256(passphrase).digest()
    IV = Random.new().read(BLOCK_SIZE)
    aes = AES.new(key, AES.MODE_CBC, IV)
    return base64.b64encode(IV + aes.encrypt(pad(message)))

def decrypt(encrypted, passphrase):
    key = hashlib.sha256(passphrase).digest()
    encrypted = base64.b64decode(encrypted)
    IV = encrypted[:BLOCK_SIZE]
    aes = AES.new(key, AES.MODE_CBC, IV)
    return unpad(aes.decrypt(encrypted[BLOCK_SIZE:]))


if __name__ == '__main__': 
    pruebaEncrypt = encrypt("canción", "español")
    print "encrypt: ", pruebaEncrypt
    pruebaDecrypt = decrypt(pruebaEncrypt,"español")
    print pruebaDecrypt
