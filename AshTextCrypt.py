from typing import Union
import Ash

class Crypt():
    def __init__(self,text: Union[str,bytes],key : str):
        self.text = text
        self.key = key

    @staticmethod
    def genkey() -> str:
        return Ash.Enc.genMainkey()

    @staticmethod
    def keyverify(key: str) -> int:
        if isinstance(key, str):
            a = bytes.fromhex(key.strip())
            if len(a) == 64:
                return 1
            else:
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
                    a = dec_instance.decToBytes()
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
    k = '818b5e3bb5a19e32cf3338c82f94015817bcc605f6ad0025840b3eb64853a2df'
    a = Crypt('test1',k)
    print(a.encrypt()[1])
