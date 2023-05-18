from typing import Union
import string
from cryptography.fernet import Fernet
import base64
import secrets


class Crypt():
    def __init__(self,text,key):
        self.text = text
        self.key = key

    @staticmethod
    def genkey() -> string:
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
    def changeform(key : string) -> Union [ bytes , int ]:
        try :
            sanitized_key = key.strip()[2:-1].encode()
            return sanitized_key
        except AttributeError :
            return 0
    @staticmethod
    def bytes_verify(key : bytes) -> int :
        try:
            testkey = base64.urlsafe_b64decode(key.strip())
            if len(testkey) == 32:
                return 1
        except Exception:
            return 0

    @staticmethod
    def str_verify(key: string) -> int:
        if isinstance(key, str):
            if len(key.strip()) == 32:
                return 1
            else:
                return 0
        else:
            return 2

    def encrypt(self) -> tuple :
            if self.text:
                try:
                    fernet1 = Fernet(self.key)
                    new_content = fernet1.encrypt(self.text.encode())
                    output = new_content.decode()
                    return 1,output
                except:
                    output = 'Error'
                    return 0,output
            else:
                return 0.0,0.0

    def decrypt(self) -> tuple :
        if self.text:
                try:
                    dec_instance = Fernet(self.key)
                    a = dec_instance.decrypt(self.text)
                    output = (a.decode())
                    return 1,output
                except Exception:
                    output = (self.text)
                    return 0,output
        else:
            return 0.0,0.0

    def __str__(self):
        return f'Encrypting/Decrypting Text {(self.text)[:8]}.. With {self.key} Key '
    def __repr__(self):
        return f'{self.__class__.__name__}({(self.text)[:8]},{self.key})'

if __name__ == '__main__':
    k = b'Ashreeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef='
    a = Crypt('hello wold',k)
    print(a.encrypt()[1])
