from Crypto.PublicKey import RSA

clave_privada = RSA.generate(4096)
clave_pública = clave_privada.publickey()

with open("Clave_privada.pem", "wb") as f:
	f.write(clave_privada.export_key())
with open("Clave_Pública.pem", "wb") as f:
	f.write(clave_pública.export_key())
print("\033[36m[***] PARES DE LLAVES GENERADAS Y GUARDADAS EN ARCHIVOS .PEM [***]\033[0m")

