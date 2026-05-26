import qrcode
from qrcode.constants import ERROR_CORRECT_H

url = "https://d-jacki.github.io/matrimonio-menu/"

qr = qrcode.QRCode(
    version=None,
    error_correction=ERROR_CORRECT_H,
    box_size=20,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
img.save("menu-qr.jpg", "JPEG", quality=95, optimize=True)

print(f"Size: {img.size}")
