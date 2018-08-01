# -*- coding: utf-8 -*-
# -*- coding: latin-1 -*-
import os, sys
import binascii
from Crypto.Cipher import AES
from hashlib import md5
import base64
from base64 import b64decode
from base64 import b64encode

KEY = '65910B1141CA4D186690392F322D5F69'
IV = '12AD FG RT IV239'
randm = os.urandom(8)
IV = binascii.hexlify(randm);
#IV = str.encode(IV)
MODE = AES.MODE_CFB
BLOCK_SIZE = 16
SEGMENT_SIZE = 128


def bytes_to_key(data, salt="12345678"):
    # Simplified version of M2Crypto.m2.bytes_to_key(). Based on:
    # https://github.com/ajmirsky/M2Crypto/blob/master/M2Crypto/EVP.py#L105
    # http://stackoverflow.com/questions/8008253/c-sharp-version-of-openssl-evp-bytestokey-method
    assert len(salt) == 8, len(salt)
    data += salt
    key = md5(data).digest()
    key += md5(key + data).digest()
    return key

def encrypt(key, iv, plaintext):
    aes = AES.new(key, MODE, iv, segment_size=SEGMENT_SIZE)
    plaintext = _pad_string(plaintext)
    encrypted_text = aes.encrypt(plaintext)
    return binascii.b2a_hex(encrypted_text).rstrip().decode('utf-8')


def decrypt(key, iv, encrypted_text):
    
    
    enc = b64decode(encrypted_text)
    iva = enc[:16]
    encrypted_text_bytes = binascii.a2b_hex(encrypted_text)
    aes = AES.new(key, MODE, iva, segment_size=SEGMENT_SIZE)
    decrypted_text = aes.decrypt(encrypted_text_bytes)
    decrypted_text = _unpad_string(decrypted_text).decode('utf-8')
    return decrypted_text


def _pad_string(value):
    length = len(value)
    pad_size = BLOCK_SIZE - (length % BLOCK_SIZE)
    return value.ljust(length + pad_size, '\x00')


def _unpad_string(value):
    while value[-1] == '\x00':
        value = value[:-1]
    return value


if __name__ == '__main__':
    input_plaintext = 'Av. Las Vías 73, Edif 15'
    #textEncryptedJS = 'ba01f26fa42306aed104c621a583eac3b10b52b0c65aeeb6930954c834993067'
    encrypted_text = encrypt(KEY, IV, input_plaintext)
    decrypted_text = decrypt(KEY, IV, encrypted_text)
    print encrypted_text
    print decrypted_text
    #assert decrypted_text == input_plaintext