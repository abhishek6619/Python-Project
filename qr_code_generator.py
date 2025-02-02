import qrcode
import os

def generate_qr(data, filename):
    project_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Generated-Image")
    
    os.makedirs(project_folder, exist_ok=True)
    
    filepath = os.path.join(project_folder, filename)
    
    qr = qrcode.make(data)
    qr.save(filepath)
    
    print(f"QR Code saved as '{filepath}'")

# Get user input
data_type = input("Enter 'text' or 'url' to generate a QR code: ").lower()

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
