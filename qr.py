import qrcode
from qrcode.image.pure import PymagingImage

import json
with open('/Users/boesene/Desktop/all.json', 'r') as f:
    data = json.load(f)

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=0,
)
qr.add_data(json.dumps(data))
qr.make(fit=True)

img = qr.make_image(fill_color="#333333", back_color="white")
img.save("qr.png")
