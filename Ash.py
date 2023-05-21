
''' STILL IN THE WORKS '''
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, hmac
import bcrypt
import os
import base64

class Ash:
    def __init__(self, message: str, mainkey: str):
        self.message = message
        self.mainkey = mainkey
        self.iv = os.urandom(16)
        self.salt = os.urandom(16)
        self.pepper = os.urandom(16)
        self.iterations = 100
        self.encKey = self.derkey1(self.mainkey, self.salt, self.iterations)
        self.hmac_k = self.derkey2(self.mainkey,self.pepper,self.iterations)
    @staticmethod
    def derkey1(mainkey: str, salt: bytes, iterations: int) -> bytes:
        hmac_k = bcrypt.kdf(
            password=mainkey.encode('UTF-8'),
            salt=salt,
            desired_key_bytes=32,
            rounds=iterations
        )
        return hmac_k

    @staticmethod
    def derkey2(mainkey: str, pepper: bytes, iterations: int) -> bytes:
        encKey = bcrypt.kdf(
            password = mainkey.encode('UTF-8'),
            salt = pepper,
            desired_key_bytes = 32,
            rounds= iterations
        )
        return encKey

    @staticmethod
    def genkey():
        return os.urandom(64).hex()

    def mode(self):
        return modes.CBC(self.iv)

    def cipher(self):
        return Cipher(algorithms.AES(key=self.encKey),mode=self.mode(), backend=default_backend())

    def cipher_encryptor(self):
        return self.cipher().encryptor()

    def padded_message(self):
        padder = padding.PKCS7(128).padder()
        return padder.update(self.message.encode('UTF-8')) + padder.finalize()
    def ciphertext(self):
        return self.cipher_encryptor().update(self.padded_message()) + self.cipher_encryptor().finalize()

    def HMAC(self):
        h = self.hmac_k
        h = hmac.HMAC(h, hashes.SHA512())
        h.update(self.ciphertext())
        return h.finalize()

    def combined_output(self)->bytes:
        return  self.HMAC() + self.iv + self.salt + self.pepper + self.ciphertext()

    def encrypt(self)->str:
        return base64.urlsafe_b64encode(self.combined_output()).decode('UTF-8')

if __name__ == '__main__':
    k512 = '818b5e3bb5a19e32cf3338c82f94015817bcc605f6ad0025840b3eb64853a2df'
    testmessage = 'Hello World !'

    a = Ash(testmessage, k512)
    b = a.combined_output()
    c = a.encrypt()
    print(b)
    print(a.HMAC().__len__())
    print(a.HMAC())
    print(b[:64])
    print(a.iv.__len__())
    print(a.iv)
    print(b[64:80])
    print(a.salt.__len__())
    print(a.salt)
    print(b[80:96])
    print(a.pepper.__len__())
    print(a.pepper)
    print(b[96:112])
    print(a.ciphertext().__len__())
    print(a.ciphertext())
    print(b[112:])
