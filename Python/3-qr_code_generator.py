import qrcode

data = input("Enter a text or URL: ").strip()
filename = input("Enter a file name: ").strip()

qr = qrcode.QRCode(box_size = 10, border = 4)
qr.add_data(data)

image = qr.make_image(fill_color = "black", back_color = "white")
image.save(filename)

print(f"QR code saved as {filename}")

