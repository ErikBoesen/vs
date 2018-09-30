import qrcode
from qrcode.image.pure import PymagingImage

import json
import csv
with open('/Users/boesene/Desktop/data.csv', 'r') as f:
    data = f.read()

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=0,
)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="#333333", back_color="white")
img.save("qr.png")
