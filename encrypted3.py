import binascii
from Crypto.Cipher import AES
from base64 import b64decode
from base64 import b64encode
from Crypto import Random

KEY = '65910B1141CA4D186690392F322D5F69'
IV = '12aD FG RT IV239';
MODE = AES.MODE_CFB
BLOCK_SIZE = 16
SEGMENT_SIZE = 128

def encrypt(key, iv, plaintext):
    aes = AES.new(key, MODE, iv, segment_size=SEGMENT_SIZE)
    plaintext = _pad_string(plaintext)
    encrypted_text = (iv + aes.encrypt(plaintext))
    return binascii.b2a_hex(encrypted_text).rstrip()
    
def decrypt(key, iv, encrypted_text):
    aes = AES.new(key, MODE, iv, segment_size=SEGMENT_SIZE)
    encrypted_text = b64decode(encrypted_text)
    #encrypted_text_bytes = binascii.a2b_hex(encrypted_text)
    decrypted_text = aes.decrypt(encrypted_text_bytes)
    decrypted_text = _unpad_string(decrypted_text).decode('utf-8')
    return decrypted_text



def _unpad_string(value):
    while value[-1] == '\x00':
        value = value[:-1]
    return value

def _pad_string(value):
    length = len(value)
    pad_size = BLOCK_SIZE - (length % BLOCK_SIZE)
    return value.ljust(length + pad_size, '\x00')

if __name__ == '__main__': 
    input_plaintext = "soy el string a encriptar"
    encrypted_text = encrypt(KEY, IV, input_plaintext)
   # decrypted_text = decrypt(KEY, IV, encrypted_text)
    print encrypted_text
    #print decrypted_text
