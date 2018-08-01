# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
from Crypto import Random
import pkcs7
import hashlib
import base64


class Encryption:

    def __init__(self):
        pass

    def Encrypt(self, PlainText, SecurePassword):
        pw_encode = SecurePassword.encode('utf-8')

        key = hashlib.sha256(pw_encode).digest()
        iv = Random.new().read(AES.block_size)

        cipher = AES.new(key, AES.MODE_CBC, iv)
        pad_text = pkcs7.PKCS7Encoder().encode(PlainText)
        msg = iv + cipher.encrypt(pad_text)

        EncodeMsg = base64.b64encode(msg)
        return EncodeMsg

    def Decrypt(self, Encrypted, SecurePassword):
        decodbase64 = base64.b64decode(Encrypted.decode("utf-8"))
        pw_encode = SecurePassword.encode('utf-8')

        iv = decodbase64[:AES.block_size]
        key = hashlib.sha256(pw_encode).digest()

        cipher = AES.new(key, AES.MODE_CBC, iv)
        msg = cipher.decrypt(decodbase64[AES.block_size:])
        pad_text = pkcs7.PKCS7Encoder().decode(msg.decode('utf-8'))

        return pad_text

##########################################################################################
##########################################################################################
encr = Encryption()

texto = base64.b64encode('texto en español'.encode('utf-8')).decode('utf-8')

en = encr.Encrypt(texto, 'key')

de = encr.Decrypt(en, 'key')

textofinal = base64.b64decode(de).decode('utf-8')

print(textofinal)
