import qrcode
import os

def generate_qr_code(link, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(file_name)
    print(f"QR code generated and saved as '{file_name}'")

def get_next_file_name(base_name, extension):
    index = 1
    while True:
        file_name = f"{base_name}{index}{extension}"
        if not os.path.exists(file_name):
            return file_name
        index += 1

if __name__ == "__main__":
    link = input("Insert link to generate QR code: ")
    base_name = "qrcode"
    extension = ".jpg"
    file_name = get_next_file_name(base_name, extension)
    generate_qr_code(link, file_name)
