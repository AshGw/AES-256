
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
        self.display = f'Iterations must be between 50 and 100000. RECEIVED : {num}.\nPossible incomplete message '
        super().__init__(self.display)

class MessageTamperingError(Exception):
    def __init__(self):
        self.display = 'HMAC mismatch ! Message has been tampered with'
        super().__init__(self.display)

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
    mainkey = '818b5e3bb5a19e32cf3338c82f94015817bcc605f6ad0025840b3eb64853a2df'
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

    ''' DEC '''

    msg_b = b'\xf0\x8by\x19\x9cy@\x1c!y\r\xe7\xcf\x99q;5\x15\xb9\xfc\x1f\x12\xac7\xc4\x1f\xfagK_K\xb2\xe1\'YR\xc8\x83W\xf4ck\x07P\x91\xe8\x8fV\xbe\x81M\xda\x9e\xa3\xcbz\x8f\xe0\xba+>MFYX\xf0\x8d\xa8x\x19\xdb\xe4\xc9\xa5\x84\xbc\x1f\x95Mq\xe8T>e\x16[\xfa\x0c\n\x88c\t\xbe\xa6>\xe1\xfa18K\xb0e\x04\xd2\xa3\xed\xe4\xdeA\xb3\xfe\xd4\x00\x00\x002\x06S\xe9\xe2\xb3\xe0\x994\x02:hq\xa8^\x90A\x14K\xb1\x8d\xda"\xee\xaf|\xda\xb6\xad\x07\xa1\xc9H'
    msg_s = 'ewLVzwKCGEQaFlklltFrbKrn-ij63xkreHiFwPPP37omctiGyP6AErj1oEIoEYgPLGHeVUWG9u4kUWw1V_2lGZw8jUQgd3EhncJfoUV9gc6GRTwjA4AdN3vulWkXNlWWtBTsHlw79oIWbQX-GjqLWgAAADLXjpcgBXJqLrPW72RqW49euE5foFvSrTkUxWqsL75fHA=='
    key = '818b5e3bb5a19e32cf3338c82f94015817bcc605f6ad0025840b3eb64853a2df'
    ins = Dec(msg_b, key)
    print(ins.decToBytes())

