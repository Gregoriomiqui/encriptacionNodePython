# -*- coding: utf-8 -*-
# -*- coding: latin-1 -*-
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
backend = default_backend()
key = os.urandom(32)
print("KEY: ", key)

#key = '65910B1141CA4D186690392F322D5F69'.encode()
iv = os.urandom(16)
print("IV: ", iv)

#iv = '12AD FG RT IV239'.encode()
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
encryptor = cipher.encryptor()
#ct = encryptor.update(b"a secret message") + encryptor.finalize()
import base64
b64data = base64.b64encode("Está es una canción".encode('utf-8')).decode('utf-8')
ct = encryptor.update(pad16(b64data).encode()) + encryptor.finalize()
decryptor = cipher.decryptor()
print(ct)
msg = decryptor.update(ct) + decryptor.finalize()

print(msg)
print(base64.decodebytes(msg).decode())