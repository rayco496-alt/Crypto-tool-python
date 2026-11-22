from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
import base64

print("\033[35m___FIRMAR MENSAJE___\033[0m")

mensaje = input("Mensaje: ")
mensaje_hash=SHA256.new(mensaje.encode())

archivo_clave_privada=input("Archivo de Clave Privada: ")
clave_privada=RSA.import_key(open(archivo_clave_privada).read())

firma = pkcs1_15.new(clave_privada).sign(mensaje_hash)

print("\033[35m---FIRMA EXITOSA---\033[0m")
print(f"\n\033[33mFIRMA: {base64.b64encode(firma).decode()} (base64)\033[0m")

with open("archivo_de_firma.bin", "wb") as f:
	f.write(firma)
