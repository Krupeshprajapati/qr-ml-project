import qrcode

# url = "http://192.168.1.71:5000/scan"
# url = "https://abcd-xyz.ngrok-free.app/scan"
# url = "https://yourapp.onrender.com/scan"

# url = "https://qr-ml-project.onrender.com/scan"
# url = "https://qr-ml-projectt.vercel.app/scan"
# url = "https://qr-ml-projectt.vercel.app/scan"
url = "https://qr_project.up.railway.app/scan"

img = qrcode.make(url)
img.save("qr_code.png")

print("QR Code Created")

