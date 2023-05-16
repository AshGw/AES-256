import qrcode
from typing import Union


def fqr(text : str) -> Union [int,tuple] : 
    try:
        with open(text,'r') as f :
            x = f.read()
        qr = qrcode.QRCode(version = 40,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=20,border=1)
        qr.add_data(x)
        qr.make(fit=True)
        img = qr.make_image(fill_color = "black", back_color="white")
        img.save(("qrv40.png"))
        img.show()
        return 1

    except Exception as e :
        return (0,e)


def tqr(text : str) -> Union [int,tuple] :
    try:
        x = text.strip()
        qr = qrcode.QRCode(version = 10,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=20,border=1)
        qr.add_data(x)
        qr.make(fit=True)
        img = qr.make_image(fill_color = "black", back_color="white")
        img.save(("qrv10.png"))
        img.show()
        return 1

    except Exception as e :
        return (0,e)


if __name__ == '__main__':
    tqr('Text here')
    fqr('File name here')
