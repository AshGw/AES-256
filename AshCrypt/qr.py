import qrcode
from typing import Union


def tqr(text: str) -> Union[int, tuple]:
    try:
        x = text.strip()
        qr = qrcode.QRCode(
            version=10,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=20,
            border=1)
        qr.add_data(x)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(("qrv10.png"))
        img.show()
        return 1

    except Exception as e:
        return (0, e)

