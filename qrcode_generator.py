# require to install QRcode library
# https://pypi.org/project/qrcode/
# There is a lot more examples on that web page


import qrcode

img = qrcode.make("https://bit.ly/3jkjUo8")

img.save("myQRcode.png")
img.show()
