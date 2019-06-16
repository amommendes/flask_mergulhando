import qrcode
import sys

def create_qrcode(data, file_path):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_H,
        box_size = 10,
        border = 4,
    )
    # Add data
    qr.add_data(data)
    qr.make(fit=True)
    # Create an image from the QR Code instance
    img = qr.make_image()
    img.save(file_path)

if __name__ == "__main__":

    data = sys.argv[1]
    file_path = sys.argv[2]
    print(data, file_path)
    create_qrcode(data,file_path)