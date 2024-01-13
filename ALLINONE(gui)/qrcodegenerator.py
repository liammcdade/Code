import qrcode

def generate_qr_code(url, file_path):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add data to the QR code
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save(file_path)

if __name__ == "__main__":
    # Example usage
    website_url = input("Enter the website URL for the QR code (full address only): ")
    qr_code_file_path = "example_qr_code.png"

    generate_qr_code(website_url, qr_code_file_path)
    print(f"QR code generated and saved to {qr_code_file_path}")
