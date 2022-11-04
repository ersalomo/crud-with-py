import qrcode


def generate_qrcode(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=12,
        border=4)

    qr.add_data(url)
    qr.make(fit=1)
    img = qr.make_image(fill_color='black', back_color='white')
    img.save('my-qr.png')


generate_qrcode('https://www.instagram.com/rrzlmx/?hl=jpn')
