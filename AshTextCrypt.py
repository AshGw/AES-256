from typing import Union
import Ash


class KeyError(Exception):
    def __init__(self):
        self.display = 'Key must be 512 Bit long !'
        super().__init__(self.display)

class Crypt():
    def __init__(self,text: Union[str,bytes],key : str):
        self.text = text
        if self.keyverify(key) == 1:
            self.key = key
        else:
            raise KeyError()

    @staticmethod
    def genkey() -> str:
        return Ash.Enc.genMainkey()

    @staticmethod
    def keyverify(key: str) -> int:
        if isinstance(key, str):
            try :
                a = bytes.fromhex(key.strip())
                if len(a) == 64 :
                    return 1
            except Exception :
                return 0

        else:
            return 2

    def encrypt(self) -> tuple :
            if self.text:
                try:
                    ins = Ash.Enc(self.text,self.key)
                    new_content = ins.encToStr()
                    return 1,new_content
                except:
                    output = 'E'
                    return 0,output
            else:
                return 0.0,0.0

    def decrypt(self) -> tuple :
        if self.text:
                try:
                    dec_instance = Ash.Dec(message=self.text,mainkey=self.key)
                    a = dec_instance.decToStr()
                    output = (a)
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
    k = 'd5d717f57933ad21725888d3451a9cd7a565dfda677fe92fd8ff9e9c3a36d1496af58c17de2b77d4d3ea6d8791b27350fea0af3ad2610d38c8cb12a29fda4bcf'
    a = Crypt(b'test1',k)
    print(a.encrypt()[1])
