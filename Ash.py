
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
        self.salt = os.urandom(16)
        self.pepper = os.urandom(16)
        self.iterations = 500
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
    
    @staticmethod
    def iv():
        return os.urandom(16)
    def mode(self):
        return modes.CBC(self.iv())

    def padded_message(self):
        padder = padding.PKCS7(128).padder()
        return padder.update(self.message.encode('UTF-8')) + padder.finalize()

    def cipher(self):
        cipher = Cipher(algorithms.AES(self.encKey), self.mode(), backend=default_backend())
        return cipher

    def cipher_encryptor(self):
        return self.cipher().encryptor()

    def ciphertext(self):
        return self.cipher_encryptor().update(self.padded_message()) + self.cipher_encryptor().finalize()

    def HMAC(self):
        h = self.hmac_k
        h = hmac.HMAC(h, hashes.SHA512())
        h.update(self.ciphertext())
        return h.finalize()

    def combined_output(self):
        return  self.HMAC() + self.iv() + self.salt + self.pepper + self.ciphertext()

    def encrypt(self):
        return base64.urlsafe_b64encode(self.combined_output()).decode('UTF-8')

if __name__ == '__main__':
    
    k512 = '818b5e3bb5a19e32cf3338c82f94015817bcc605f6ad0025840b3eb64853a2df'
    testmessage = 'Hello World !'

    a = Ash(testmessage, k512)
    b = a.encrypt()
    print(b)
    print(b.__len__())
    print(len(a.encKey))
