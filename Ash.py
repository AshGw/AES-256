
''' STILL IN THE WORKS '''
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, hmac
import bcrypt
import os
import base64

class Enc:
    def __init__(self, message: str, mainkey: str)->None:
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
            password = mainkey.encode('UTF-8'),
            salt = pepper,
            desired_key_bytes = 32,
            rounds= iterations
        )
        return hmac_k

    @staticmethod
    def genMainkey():
        return os.urandom(64).hex()

    def mode(self):
        return modes.CBC(self.iv)

    def cipher(self):
        return Cipher(algorithms.AES(key=self.encKey),mode=self.mode(), backend=default_backend())

    def cipher_encryptor(self):
        return self.cipher().encryptor()

    def padded_message(self)->bytes:
        padder = padding.PKCS7(128).padder()
        return padder.update(self.message.encode('UTF-8')) + padder.finalize()
    
    def ciphertext(self):
        return self.cipher_encryptor().update(self.padded_message()) + self.cipher_encryptor().finalize()

    def HMAC(self):
        h = self.hmac_k
        h = hmac.HMAC(h, hashes.SHA512())
        h.update(self.ciphertext())
        return h.finalize()

    def encToBytes(self)->bytes:
        return  self.HMAC() + self.iv + self.salt + self.pepper + self.ciphertext()

    def encToStr(self)->str:
        return base64.urlsafe_b64encode(self.encToBytes()).decode('UTF-8')
    
 class Dec():
    def __init__(self,message : bytes , key : str):
        self.message = message
        self.key = key
        self.rec_hmac = self.message[:64]
        self.rec_iv = self.message[64:80]
        self.rec_salt = self.message[80:96]
        self.rec_pepper = self.message[96:112]
        self.rec_ciphertext = self.message[112:]
        self.iterations = 100
        self.decKey = self.derkey2(self.key,self.rec_salt,self.iterations)
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
        return Cipher(algorithms.AES(key=self.decKey),mode=self.mode(),backend=default_backend())

    def cipher_decryptor(self):
        return self.cipher().decryptor()

    def unpadded_message(self):
        # unpadder = padding.PKCS7(128).unpadder()
        # return unpadder.update(self.rec_ciphertext) + unpadder.finalize()
        return self.rec_ciphertext

    def decToBytes(self)->bytes:
        return self.cipher_decryptor().update(self.unpadded_message()) + self.cipher_decryptor().finalize()

    def decToStr(self)->str:
        return (self.palaintext_bytes().decode('UTF-8'))

