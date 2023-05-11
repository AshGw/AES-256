import qrcode

def makeqr(text):
    with open(text,'r') as f :
        x = f.read()
    qr = qrcode.QRCode(version = 40,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=20,border=1)
    qr.add_data(x)
    qr.make(fit=True)
    img = qr.make_image(fill_color = "black", back_color="white")
    img.save(("qrv40.png"))
    img.show()

if __name__ == '__main__':
    makeqr('test1')