import qrcode as qr
img=qr.make("https://www.youtube.com/watch?v=FOGRHBp6lvM&t=66s")
img.save("youtube.png")

import qrcode 
form PIL import Image

qr= qrcode.QRCode(version=1,
                  error_correction=qecode.constants.ERROR_CORRECT_H
                #   box_size=18,border=3,)
                box_size=18,border=18,)
qr.add_data("https://www.youtube.com/watch?v=FOGRHBp6lvM&t=66s")
qr.make(fit=True)
# img=qr.make_image(fill_color="red",back_color="blue")
img=qr.make_image(fill_color="red",back_color="white")


img.save("youtube.png")




a=34
c==354
d=31
h=46

print(a*a*c*d+h)
