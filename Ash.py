from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, hmac
from typing import Union
import hmac as hmc
import bcrypt
import base64
import struct
import time
import os

class IterationsOutofaRangeError(Exception):
    def __init__(self,num):
        self.display = f'Iterations must be between 50 and 100000. RECEIVED : {num} '
        super().__init__(self.display)

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
        self.iterations = 50
        if self.iterations < 50 or self.iterations > 100000:
            raise IterationsOutofaRangeError(self.iterations)
        self.encKey = self.derkey(self.mainkey, self.salt, self.iterations)
        self.hmac_key = self.derkey(self.mainkey, self.pepper, self.iterations)

    @staticmethod
    def derkey(mainkey: str, salt_pepper: bytes, iterations: int) -> bytes:
        return bcrypt.kdf(
            password = mainkey.encode('UTF-8'),
            salt = salt_pepper,
            desired_key_bytes = 32,
            rounds = iterations)

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
        return self.HMAC() + self.iv + self.salt + self.pepper + self.setupIterations() + self.ciphertext()

    def encToStr(self) -> str:
        return base64.urlsafe_b64encode(self.encToBytes()).decode('UTF-8')


class MessageTamperingError(Exception):
    def __init__(self):
        self.display = 'HMAC mismatch ! Message has been TAMPERED with ,\n or Possible key difference'
        super().__init__(self.display)

class Dec:
    def __init__(self,message: Union[str, bytes], mainkey: str):
        if isinstance(message, str):
            m = message.encode('UTF-8')
            self.message = base64.urlsafe_b64decode(m)
        elif isinstance(message, bytes):
            self.message = message
        self.key = mainkey
        self.rec_hmac = self.message[:64]
        self.rec_iv = self.message[64:80]
        self.rec_salt = self.message[80:96]
        self.rec_pepper = self.message[96:112]
        self.rec_iterations = struct.unpack('!I', self.message[112:116])[0]
        if self.rec_iterations < 50 or self.rec_iterations > 100000:
            raise IterationsOutofaRangeError(self.rec_iterations)
        self.rec_ciphertext = self.message[116:]
        self.decKey = Enc.derkey(self.key, self.rec_salt, self.rec_iterations)
        self.hmac_k = Enc.derkey(self.key, self.rec_pepper, self.rec_iterations)
        if self.verifyHMAC() is False :
            raise MessageTamperingError()
    def actualHMAC(self):
        h = self.hmac_k
        h = hmac.HMAC(h, hashes.SHA512())
        h.update(self.rec_ciphertext)
        return h.finalize()

    def verifyHMAC(self)->bool:
        return hmc.compare_digest(self.actualHMAC(), self.rec_hmac)

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
    message = 'Hello'
    key = Enc.genMainkey()
    instance1 = Enc(message = message,mainkey = key)
    print(instance1.encToBytes())