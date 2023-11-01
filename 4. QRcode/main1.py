import qrcode

qr_data = 'www.google.com'
qr_img = qrcode.make(qr_data)

save_path = '4. QRcode\\' + qr_data + '.png'


