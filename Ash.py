
''' STILL IN THE WORKS '''

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

class IterationsOutofaRangeErrorE(Exception):
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
            raise IterationsOutofaRangeErrorE(self.iterations)
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



class IterationsOutofaRangeErrorD(Exception):
    def __init__(self,num):
        self.display = f'Iterations must be between 50 and 100000. RECEIVED : {num}'
        super().__init__(self.display)

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
            raise IterationsOutofaRangeErrorD(self.rec_iterations)
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

    ''' ENC '''

    message1 = 'Hello there testing if it works'
    message2 = b'Hello this is bytes now'
    mainkey = 'c3066e464350e68a144d6be3e35c879eac1b9f360139443ee3d9e1960725d6a4d3379af0a35b6a07d083ecc29c4ba03767ad6d48b8e9c20d319dd459da52a91a'
    print(Enc.genMainkey())
    t1 = time.perf_counter()
    ins = Enc(message=message1, mainkey=mainkey)
    a = ins.encToBytes()
    print(a)
    print(a[:64] == ins.HMAC())
    print(a[64:80] == ins.iv)
    print(a[80:96] == ins.salt)
    print(a[96:112] == ins.pepper)
    print(a[112:116] == ins.setupIterations())
    print(a[116:] == ins.ciphertext())
    print(ins.setupIterations())
    print(type(ins.setupIterations()))
    print(ins.setupIterations().__len__())
    print(ins.encToBytes())
    c = ins.setupIterations()
    b = ins.encToBytes()[112:116]
    print(c == b)
    t2 = time.perf_counter()
    print(t2 - t1)
    print(ins.encToStr())
    print(ins.encToBytes())

    ''' DEC '''

    msg_b =b'\x03;\xf7\x89\xef\xa9s\x16\xd2\x0c\n5\x05\x1cQ\xee.-\xa7\xcf\xf4\xb2\xc8#\xfe\x19\x1e\xd6\x98({J=\xed\xa0+,\xecJ\x9a\x02\x97\xda\x93\x99K6\xf9f\xa5\xda \x80h\x82\xc9\xeeU\xec\x98\xc1\xcb\nJH\xca\xf1\xf2M/=\x07hS\xcd \xdc\x8e\x0b\x8bS\x90 \xe8\xbd\xcb\x1a\xad\xde\x85\x17\x89\xa7\x02~\xde\x02D\x1d\xb9OC\xceO:\xdc\xc7\x99\xd7\xd4ru\x00\x00\x002$\x94\xa8\xc1\xa1i\x94\xac\xa8\xde\x82\x04\x94\xbc\x82W\xbb\xed\xe7\x1dY\xbe\xeb"A\xe4\xab"\xfe\xb8\xcb\xac'
    msg_s = 'ewLVzwKCGEQaFlklltFrbKrn-ij63xkreHiFwPPP37omctiGyP6AErj1oEIoEYgPLGHeVUWG9u4kUWw1V_2lGZw8jUQgd3EhncJfoUV9gc6GRTwjA4AdN3vulWkXNlWWtBTsHlw79oIWbQX-GjqLWgAAADLXjpcgBXJqLrPW72RqW49euE5foFvSrTkUxWqsL75fHA=='
    key = 'c3066e464350e68a144d6be3e35c879eac1b9f360139443ee3d9e1960725d6a4d3379af0a35b6a07d083ecc29c4ba03767ad6d48b8e9c20d319dd459da52a91a'
    t3 = time.perf_counter()
    ins = Dec(msg_b, key)
    print(ins.decToBytes())
    t4 = time.perf_counter()
    print(t4-t3)
