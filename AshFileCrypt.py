import Ash
import os

class KeyError(Exception):
    def __init__(self):
        self.display = 'Key must be 512 Bit long !'
        super().__init__(self.display)

class CryptFile():
    def __init__(self,filename,key):
        self.filename = filename
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
            a = bytes.fromhex(key.strip())
            if len(a) == 64:
                return 1
            else:
                return 0
        else:
            return 2
    def encrypt(self) -> int :
        if not os.path.exists(self.filename):
            return 3
        else :
            with open(self.filename, 'rb') as f:
                filecontent = f.read()
            with open(self.filename, 'wb') as f:
                if filecontent:
                    try:
                        ins = Ash.Enc(message=filecontent,mainkey=self.key)
                        new_content= ins.encToBytes()
                        f.write(new_content)
                        return 1
                    except:
                        f.write(filecontent)
                        return 0
                else:
                    return 2

    def decrypt(self) -> int :
        if not os.path.exists(self.filename):
            return 3
        else :
            with open(self.filename, 'rb') as f:
                enc_content = f.read()
            if enc_content:
                with open(self.filename, 'wb') as f:
                    try:
                        ins = Ash.Dec(message=enc_content,mainkey=self.key)
                        a = ins.decToBytes()
                        f.write(a)
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
    print(Ash.Enc.genMainkey())
    key = 'd5d717f57933ad21725888d3451a9cd7a565dfda677fe92fd8ff9e9c3a36d1496af58c17de2b77d4d3ea6d8791b27350fea0af3ad2610d38c8cb12a29fda4bcf'
    target = CryptFile('qrv10.png', key)
    print(target.encrypt())


