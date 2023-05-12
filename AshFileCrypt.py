from typing import Union
import string
from cryptography.fernet import Fernet
import base64
import secrets



class CryptFiles():
    def __init__(self,filename,key):
        self.filename = filename
        self.key = key

    @staticmethod
    def key_gen() -> string:
        key = ''
        for _ in range(32):
            mysequence = string.ascii_letters + string.digits
            key = key + secrets.choice(mysequence)
        return key

    @staticmethod
    def getready(key: string) -> Union [ bytes , int ]:
        try :
            key = base64.urlsafe_b64encode(key.strip().encode())
            return key
        except AttributeError :
            return 0
    @staticmethod
    def intruder_strbytes_key_sanitization(key : string) -> Union [ bytes , int ]:
        try :
            sanitized_key = key.strip()[2:-1].encode()
            return sanitized_key
        except AttributeError :
            return 0
    @staticmethod
    def intruder_bytes_key_verification(key : bytes) -> int :
        try:
            testkey = base64.urlsafe_b64decode(key.strip())
            if len(testkey) == 32:
                return 1
        except Exception:
            return 0

    @staticmethod
    def intruder_str_key_verification(key: string) -> int:
        if isinstance(key, str):
            if len(key.strip()) == 32:
                return 1
            else:
                return 0
        else:
            return 2

    def encrypt(self) -> int :
        with open(self.filename, 'r') as f:
            filecontent = f.read()
        with open(self.filename, 'w') as f:
            if filecontent:
                try:
                    fernet1 = Fernet(self.key)
                    new_content = fernet1.encrypt(filecontent.encode())
                    f.write(new_content.decode())
                    return 1
                except:
                    f.write(filecontent)
                    return 0
            else:
                return 2

    def decrypt(self) -> int :
        with open(self.filename, 'r') as f:
            enc_content = f.read()
        if enc_content:
            with open(self.filename, 'w') as f:
                try:
                    dec_instance = Fernet(self.key)
                    a = dec_instance.decrypt(enc_content)
                    f.write(a.decode())
                    return 1
                except Exception:
                    f.write(enc_content)
                    return 0
        else:
            return 2

    def __str__(self):
        return f'Encrypting/Decrypting File {self.filename} With {self.key} Key '
    def __repr__(self):
        return f'{self.__class__.__name__}({self.filename},{self.key})'

if __name__ == '__main__':
    key_byt = b'Ashreeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef='  # Bytes can be used directly (verify first)
    key_str = 'Ashreeeeeeeeeeeeeeeeeeeeeeeeeeef'               # Strings need to get ready (verify first)

    key_str = CryptFiles.getready(key_str)
    target = CryptFiles('test1.txt', key_str)
    target.decrypt()
