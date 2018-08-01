# -*- coding: utf-8 -*-
import argparse
import os
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Constantes  
BLOCK_SIZE = 16
SEGMENT_SIZE = 128

KEY= 'qweeqwertyuiopasdfghjklñzxcvbnm'
KEY = str.encode(KEY)
IV = '-.,mnbvcrrwedfgd'
IV = str.encode(IV)

# Variables globales----------------------------------------------------------------------------------------------------
backend = default_backend()
cipher = Cipher(algorithms.AES(KEY), modes.CBC(IV), backend=backend)

# ----------------------------------------------------------------------------------------------------------------------


class Aes_encryption:

    @staticmethod
    def pad(text):
        while len(text) % 8 != 0:
            text += ' '
        return text

    @staticmethod
    def pad16(text):
        while len(text) % 16 != 0:
            text += ' '
        return text

    @staticmethod
    def encrypt(plaintext):
        if plaintext is None:
            return None
        encryptor = cipher.encryptor()
        b64data = base64.b64encode(str(plaintext).encode('utf-8')).decode('utf-8')
        ct = encryptor.update(Aes_encryption.pad16(b64data).encode()) + encryptor.finalize()
        result = base64.b64encode(ct).decode('ascii')
        #return ct
        return result


    @staticmethod
    def decrypt(encrypted_text):
        if encrypted_text is None:
            print("encrypted_text is ", encrypted_text)
            return None
        result =base64.b64decode(encrypted_text.encode())
        decryptor = cipher.decryptor()
        #encrypted_text = decryptor.update(encrypted_text) + decryptor.finalize()
        encrypted_text = decryptor.update(result) + decryptor.finalize()
        return base64.decodebytes(encrypted_text).decode()

    @staticmethod
    def _pad_string(value):
        length = len(value)
        pad_size = BLOCK_SIZE - (length % BLOCK_SIZE)
        return value.ljust(length + pad_size, '\x00')

    @staticmethod
    def _unpad_string(value):
        while value[-1] == '\x00':
            value = value[:-1]
        return value


if __name__ == '__main__':
    input_plaintext = 'Mi nueva Canción de caña de azucar 37$%4'
    cifrado = Aes_encryption.encrypt(input_plaintext)
    print("tipo:",type(cifrado),"cifrado ", cifrado)

    descifrado = Aes_encryption.decrypt(cifrado)
    print(descifrado)

