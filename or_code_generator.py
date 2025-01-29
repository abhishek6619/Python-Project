import qrcode

def generate_qr(data, filename):
    qr = qrcode.make(data)

    qr.save(filename)
    print(f"QR Code saved as '{filename}'")


data_type = input(
    "Enter 'text' or 'url' to generate a QR code: "
).lower()

if data_type == "text":
    text = input("Enter the text: ")
    filename = input("Enter the filename to save the QR code (e.g., text_qr.png): ")
    generate_qr(text, filename)

elif data_type == "url":
    url = input("Enter the website URL: ")
    filename = input("Enter the filename to save the QR code (e.g., url_qr.png): ")
    generate_qr(url, filename)

else:
    print("Invalid input! Please enter 'text' or 'url'.")
