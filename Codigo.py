import qrcode

"""
'''
Instalación de librerias correspondientes para que funcione el codigo
pip install qrcode
pip install Pillow
Actualización de librerias
pip install --upgrade qrcode y de version de pip pip install --upgrade pip
nuevo sitio web de Gomsoft https://gomsoft.site/
'''
"""


# Crea un objeto QRCode
qr = qrcode.QRCode(
    version=1, # Ajusta el tamaño del código QR (1 es el más pequeño, 40 el más grande)
    error_correction=qrcode.constants.ERROR_CORRECT_L, # Ajusta el nivel de corrección de errores
    box_size=10, # Ajusta el tamaño del código QR en píxeles
    border=4 # Ajusta el grosor del borde del código QR en píxeles
)

# Agrega la URL del sitio web de Gomsoft a los datos del código QR
qr.add_data("https://gomsoft.site/")

# Genera la imagen del código QR
qr.make(fit=True)

# Convierte la imagen del código QR a PNG
#img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

img = qr.make_image(fill_color="black", back_color="white", pil=True).convert("RGB")

# Guarda la imagen con el nombre y extension correspondiente
img.save("gomsoft-qr-code.png")

