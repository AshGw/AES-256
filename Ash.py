
''' STILL IN THE WORKS '''

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, hmac
import os
import base64

class Ash:
    def __init__(self, message: str, key: str):
        self.message = message
        self.key = bytes.fromhex(key)
        self.encKey = self.key[:32]

    @staticmethod
    def genkey():
        return os.urandom(64).hex()

    def iv(self):
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
        h = self.key[32:]
        h = hmac.HMAC(h, hashes.SHA3_512())
        h.update(self.ciphertext())
        return h.finalize()

    def combined_output(self):
        return  self.HMAC() + self.iv() + self.ciphertext()

    def encrypt(self):
        return base64.urlsafe_b64encode(self.combined_output()).decode('UTF-8')
