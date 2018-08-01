from base64 import b64decode
from Crypto.Cipher import AES


if __name__ == '__main__':
    iv = 'asdfasdfasdfasdf'
    key = 'asdfasdfasdfasdfasdfasdfasdfasdf'
    encoded = b64decode('uo4h49lewUKByV5U1gTTWg==')

    dec = AES.new(key=key, mode=AES.MODE_CBC, IV=iv)
    value = dec.decrypt(encoded)
    print value