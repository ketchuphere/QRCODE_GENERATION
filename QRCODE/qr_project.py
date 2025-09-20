import qrcode as qr

img = qr.make("Hello World")
img.save("hello.png")
