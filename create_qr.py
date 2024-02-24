import qrcode

def generate_qr_code(data, file_path):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=5,
        border=2,
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save(file_path)

if __name__ == "__main__":
    # Example usage
    for i in range(1, 5 + 1):
        data_to_encode = f"K7.101.MTB.0{i}"
        output_file_path = f"{data_to_encode}.png"
        generate_qr_code(data_to_encode, output_file_path)
        print(f"QR code saved as {output_file_path}")
