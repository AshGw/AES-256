
''' STILL IN THE WORKS '''

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, hmac
import bcrypt
import os
import base64
from typing import Union
import struct
import time

class IterationsOutofRangeError(Exception):
    pass
class Enc:
    def __init__(self, message: Union[str, bytes], mainkey: str) -> None:
        if isinstance(message, str):
            self.message = message.encode()
        elif isinstance(message, bytes):
            self.message = message

        self.mainkey = mainkey
        self.iv = os.urandom(16)
        self.salt = os.urandom(16)
        self.pepper = os.urandom(16)
        self.iterations = 100
        if self.iterations < 50 or self.iterations > 100000:
            raise IterationsOutofRangeError
        self.encKey = self.derkey1(self.mainkey, self.salt, self.iterations)
        self.hmac_key = self.derkey2(self.mainkey, self.pepper, self.iterations)

    @staticmethod
    def derkey1(mainkey: str, salt: bytes, iterations: int) -> bytes:
        encKey = bcrypt.kdf(
            password=mainkey.encode('UTF-8'),
            salt=salt,
            desired_key_bytes=32,
            rounds=iterations
        )
        return encKey

    @staticmethod
    def derkey2(mainkey: str, pepper: bytes, iterations: int) -> bytes:
        hmac_key = bcrypt.kdf(
            password=mainkey.encode('UTF-8'),
            salt=pepper,
            desired_key_bytes=32,
            rounds=iterations
        )
        return hmac_key

    @staticmethod
    def genMainkey():
        return os.urandom(64).hex()

    def mode(self):
        return modes.CBC(self.iv)

    def cipher(self):
     return Cipher(algorithms.AES(key=self.encKey), mode=self.mode(), backend=default_backend())

    def cipher_encryptor(self):
        return self.cipher().encryptor()

    def padded_message(self) -> bytes:
        padder = padding.PKCS7(128).padder()
        return padder.update(self.message) + padder.finalize()

    def ciphertext(self):
        return self.cipher_encryptor().update(self.padded_message()) + self.cipher_encryptor().finalize()

    def HMAC(self):
        h = self.hmac_key
        h = hmac.HMAC(h, hashes.SHA512())
        h.update(self.ciphertext())
        return h.finalize()

    def setupIterations(self):
        iters_bytes = struct.pack('!I',self.iterations)
        return iters_bytes

    def encToBytes(self) -> bytes:
        return self.HMAC() + self.iv + self.salt + self.pepper + self.ciphertext() + self.setupIterations()

    def encToStr(self) -> str:
        return base64.urlsafe_b64encode(self.encToBytes()).decode('UTF-8')

    
    
class Dec():
    def __init__(self, message: bytes, key: str):
        self.message = message
        self.key = key
        self.rec_hmac = self.message[:64]
        self.rec_iv = self.message[64:80]
        self.rec_salt = self.message[80:96]
        self.rec_pepper = self.message[96:112]
        self.rec_ciphertext = self.message[112:]
        self.iterations = 100
        self.decKey = self.derkey2(self.key, self.rec_salt, self.iterations)
        self.hmac_k = self.derkey1(self.key, self.rec_pepper, self.iterations)

    @staticmethod
    def derkey1(mainkey: str, salt: bytes, iterations: int) -> bytes:
        encKey = bcrypt.kdf(
            password=mainkey.encode('UTF-8'),
            salt=salt,
            desired_key_bytes=32,
            rounds=iterations
        )
        return encKey

    @staticmethod
    def derkey2(mainkey: str, pepper: bytes, iterations: int) -> bytes:
        hmac_k = bcrypt.kdf(
            password=mainkey.encode('UTF-8'),
            salt=pepper,
            desired_key_bytes=32,
            rounds=iterations
        )
        return hmac_k

    def mode(self):
        return modes.CBC(self.rec_iv)

    def cipher(self):
        return Cipher(algorithms.AES(key=self.decKey), mode=self.mode(), backend=default_backend())

    def cipher_decryptor(self):
        return self.cipher().decryptor()

    def pre_unpadding_dec(self) -> bytes:
        return self.cipher_decryptor().update(self.rec_ciphertext) + self.cipher_decryptor().finalize()

    def unpadded_m(self):
        unpadder = padding.PKCS7(128).unpadder()
        return unpadder.update(self.pre_unpadding_dec()) + unpadder.finalize()

    def decToBytes(self)->bytes:
        return self.unpadded_m()

    def decToStr(self) -> str:
        return (self.unpadded_m().decode('UTF-8'))
    
    

if __name__ == '__main__':
    ''' The Encryption Testing Phase I '''
    
    message1 = 'Hello there testing if it works'
    message2 = b'Hello this is bytes now'
    mainkey = '818b5e3bb5a19e32cf3338c82f94015817bcc605f6ad0025840b3eb64853a2df'
    ins = Enc(message=message2,mainkey=mainkey)
    a = ins.encToBytes()
    print(a[:64] == ins.HMAC())
    print(a[64:80] == ins.iv)
    print(a[80:96] == ins.salt)
    print(a[96:112] == ins.pepper)
    print(a[112:] == ins.ciphertext())
    print(ins.encToBytes())
    
    ''' Now For The Decryption Testing Phase I '''
    
    rec_mess = b'3\x8c\xfe\xc6\x9a\xce\xd3\xbc\r\x89\xda\x0b\xf2\x8d(\x7f\x05\xcf\x03%\x8e\t"h\x8a7\xf0C\xb3\xdb\xbf\xc6wP\xac\x14\\\x10^\xddw\x84\xf8(?o"\x17\x84\x8e\x0c\xa5n+\x0eo\xe9Y\xf5\x16}\x13"d\xeb\x023R{\xfa\xda\xe2\x1a\xf3\xdd\x83Cur\x022\x06\x96(t\x16<\xf0\xea\xe8\x8d\x83z9y"\x14\xfb\xa5%\x92\xa8\x0eU1\xb0\xb3\xf0\ru\x94\t\xe0\x8c`\xce\xfe \xbbC\x8b \x9a\xcb6\xd6\x90\xd5\x96\x8d?\x84"\xff\xf7O=\xfex\x99#Y\xb0:'
    key = '818b5e3bb5a19e32cf3338c82f94015817bcc605f6ad0025840b3eb64853a2df'
    ins = Dec(rec_mess,key)
    print(ins.decToStr())
    

