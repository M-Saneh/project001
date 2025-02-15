import qrcode as qr
name = input("Enter the name of the file for the QR code : ")
url = input("Enter the URL or message : ")
img = qr.make(f"{url}")  #url of site that you are making a qrcode of...
img.save(f"{name}.png")