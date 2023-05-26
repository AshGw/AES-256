import Ash


class CryptFiles():
    def __init__(self,filename,key):
        self.filename = filename
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

    def encrypt(self) -> int :
        with open(self.filename, 'r') as f:
            filecontent = f.read()
        with open(self.filename, 'w') as f:
            if filecontent:
                try:
                    ins = Ash.Enc(message=filecontent,mainkey=self.key)
                    new_content= ins.encToStr()
                    f.write(new_content)
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
                    ins = Ash.Dec(message=enc_content,mainkey=self.key)
                    a = ins.decToStr()
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
    key = '818b5e3bb5a19e32cf3338c82f94015817bcc605f6ad0025840b3eb64853a2df'
    target = CryptFiles('target.txt', key)
    target.decrypt()
