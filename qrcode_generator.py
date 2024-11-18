import qrcode

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data to the QR code
data = input("Enter the data to be encoded: ")
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
filename = input("Enter the filename to save the QR code to: ")
img.save(filename + ".png")

# Display the QR code
img.show()
