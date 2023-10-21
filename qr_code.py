# import qrcode as qr

# img = qr.make("Hello, world!")
# img.save("basic.png")   


import qrcode 
from PIL import Image

qr = qrcode.QRCode(version=1,
error_correction=qrcode.constants.ERROR_CORRECT_H,
border=10,box_size=10,)

qr.add_data("Hello Python")
qr.make(fit=True)
img = qr.make_image(fill_color = "red",back_color = "white")
img.save("basic.png")