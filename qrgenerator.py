import qrcode

data = input("Enter any text or URL: ")
filename = input("Enter your filename (include extension, e.g. myqr.png): ")

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data) #add text or url 
qr.make(fit=True) #finialize 

image = qr.make_image(fill_color='black', back_color='white')
image.save(filename)

print(f"Your QR code is saved as {filename}")
