
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

    
    
class IterationsOutofaRangeError(Exception):
    pass

class Dec:
    def __init__(self,message: Union[str, bytes], key: str):
        if isinstance(message, str):
            m = message.encode('UTF-8')
            self.message = base64.urlsafe_b64decode(m)
        elif isinstance(message, bytes):
            self.message = message
        self.key = key
        self.rec_hmac = self.message[:64]
        self.rec_iv = self.message[64:80]
        self.rec_salt = self.message[80:96]
        self.rec_pepper = self.message[96:112]
        self.rec_ciphertext = self.message[112:]
        self.rec_iterations = struct.unpack('!I', self.message[-4:])[0]
        if self.rec_iterations < 50 or self.rec_iterations > 100000:
            raise IterationsOutofaRangeError
        self.decKey = self.derkey2(self.key, self.rec_salt, self.rec_iterations)
        self.hmac_k = self.derkey1(self.key, self.rec_pepper, self.rec_iterations)

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
    ''' The Encryption Testing Phase III '''
    
    message1 = 'Hello there testing if it works'
    message2 = b'Hello this is bytes now'
    mainkey = '818b5e3bb5a19e32cf3338c82f94015817bcc605f6ad0025840b3eb64853a2df'
    t1 = time.perf_counter()
    ins = Enc(message=message2,mainkey=mainkey)
    a = ins.encToBytes()
    print(a[:64] == ins.HMAC())
    print(a[64:80] == ins.iv)
    print(a[80:96] == ins.salt)
    print(a[96:112] == ins.pepper)
    print(a[112:-4] == ins.ciphertext())
    print(a[-4:] == ins.setupIterations())
    print(ins.setupIterations())
    print(type(ins.setupIterations()))
    print(ins.setupIterations().__len__())
    print(ins.encToBytes())
    c = ins.setupIterations()
    b = ins.encToBytes()[-4:]
    print(c == b)
    t2 = time.perf_counter()
    print(t2-t1)
    
    ''' Now For The Decryption Testing Phase III '''
    
    msg_b = b"\xbf\x16\xa6+\x8f~\xba\x99\x02\xc6BX\xcd+\xbf\x05r\x074\x14\x8a\xf7\xc1\x85\xe9\xb4\x95O-6\xf5;\xf4\xe3,Ge;\xe2NZ\xe7\xfa\xba\xe8\xc8\xee\x9e4\xbd\x8fr\xfe\xc8=`\xe6\xd3pW\xb0\xbe\xdb\x96\xfb]\xcf\xb3g\x08srQ\xd26=\xa0d\x99\xfd\xa9\xa4z\x7f\xda\xc2_0\xb49\xa8R'\xf5\x06^\n\xba\x82\xa8\xb2\x12H\x94\x96f\xe3\x13\xba\x0b\x9c\xa5\xe8T\xd4)k\xbd,\xfa\xc5\xd0\xc6\xba\x18!\xd8\x9a\xb6S\xace\r\xad\x15:\xf4\x18\x10\x14\xb7T;\x81\x00\x00\x002"
    msg_s = 'G5mXFJ6U_cK-niZNsB02DUznP2OINJ9B5U0wuVWTC7sFykl1u8MqrRgggpfVUqWzuRN7eCa0Dq2-14FC41KLDg0eKczG2D8ogCR_hWSDB8t-y5x8Jpum7tWAJ-MhR5iuTljIG6WOQZ_L9dyD3PJE3zEJbdNmXo3MYqh7WK0-gthBcIu6Kd-MW2LRsNyh4S22AAAAMg=='
    key = '818b5e3bb5a19e32cf3338c82f94015817bcc605f6ad0025840b3eb64853a2df'
    ins = Dec(msg_s,key)
    print(ins.decToBytes())

