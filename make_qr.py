import qrcode
site_url = "https://YOUR-USERNAME.github.io/nnc-khaled-contact/"
qrcode.make(site_url).save("NNC_Khaled_Website_QR.png")
print("QR generated for:", site_url)
