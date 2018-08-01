# -*- coding: utf-8 -*-
from Crypto import Random
from Crypto.Cipher import AES
import base64
import binascii
import random 
import os

KEY_SIZE = 32
KEY = '65910B1141CA4D186690392F322D5F69'
IV = '12aD FG RT IV239'
ENCRYPTION_KEY = b"thisisasamplepassphraseforencoding"
# PKCS5 Padding
def pad_pkcs5(text):
  try:
    length = KEY_SIZE - (len(text) % KEY_SIZE)
    return text + chr(length)*length
  except:
    print "Excepción en Padding pad_pkcs5()"

def unpad_pkcs5(text):
  try:
    pad = ord(text[-1])

    # verificando padding
    if ord(text[-pad]) != pad:
      raise ValueError('Invalid padding')
    return text[0:-ord(text[-1])]
  except ValueError as error:
    print "Excepcioón en Padding unpad_pkcs5(): %s" %error

# Encryption usando AES CBC (128-bits)
def encrypt(plaintext, passphrase, iv):
  try:
    aes = AES.new(passphrase, AES.MODE_CTR, iv)
    return base64.b64encode(aes.encrypt(plaintext)).decode('utf-8')
  except:
    print "Excepción en la encrypt()"

# Decryption usando AES CBC (128-bits)
def decrypt(ciphertext, passphrase, iv):
  try:
    decrypted = base64.b64decode(ciphertext)
    aes = AES.new(passphrase, AES.MODE_CBC, iv)
    plaintext = unpad_pkcs5(aes.decrypt(decrypted)).decode('utf-8')
    return plaintext
  except:
    print "Excepción en la decrypt()"

# Driver function
def test():
  plaintext = 'escucho una canción'
  try:		
       # Ensure that the key is no more than 16-bytes long
    KEY = ENCRYPTION_KEY[0:KEY_SIZE] if len(ENCRYPTION_KEY) > KEY_SIZE else ENCRYPTION_KEY

    # Generate initialization vector
    randm = os.urandom(8)
    IV = binascii.hexlify(randm);

    # Encrypt plain text
    encrypted = encrypt(plaintext, KEY, IV)
    print "texto encriptado: %s" %encrypted
    # Decrypt cipher text
    decrypted = decrypt(encrypted, KEY, IV)
    print "texto desencriptado: %s" %decrypted
  except:
    print "Se produjo una excepción al cifrar texto sin formato en test()"
		
# Prueba de encryption
test()