import qrcode

url = input("Ingresa el link que quieras convertir a QR: ")

img = qrcode.make(url)

img.save('qrcode.png')
print("Tu codigo QR ha sido creado, por favor revisa la carpeta.")