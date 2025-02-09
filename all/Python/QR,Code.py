import qrcode
from PIL import Image


# First QR code
img = qrcode.make("https://www.youtube.com/watch?v=FOGRHBp6lvM&t=66s")
img.save("youtube1.png")

# Second QR code with customization
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=18,
    border=18,
)
qr.add_data("https://www.youtube.com/watch?v=FOGRHBp6lvM&t=66s")
qr.make(fit=True)

img = qr.make_image(fill_color="red", back_color="white")
img.save("youtube2.png")

# Corrected variable assignments and print statement
a = 34
c = 354
d = 31
h = 46

print(a * a * c * d + h)

# Corrected variable assignment for `a`
z = 10  # Example value for z
a = z
