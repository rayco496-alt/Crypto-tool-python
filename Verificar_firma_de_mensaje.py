from Crypto.Signature import pkcs1_15
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
import base64

mensaje=input("Mensaje: ")
archivo_clave_pública=input("\nArchivo con la Clave Pública: ")
clave_pública = RSA.import_key(open(archivo_clave_pública).read())
archivo_firma=input("\nArchivo con la Firma: ")

with open(archivo_firma, "rb") as f:
	firma=f.read()

print("\033[35m---INICIANDO VERIFICACIÓN DE FIRMA---\033[0m")

mensaje_hash = SHA256.new(mensaje.encode())

try:
	pkcs1_15.new(clave_pública).verify(mensaje_hash, firma)
	print("\n\033[32m[EXITO] FIRMA VERIFICADA Y VÁLIDA\033[0m")
except (ValueError,TypeError):
	print("\n\033[31m[ALERTA] -- [ERROR]-- [FIRMA INVÁLIDA] -- [EL MENSAJE HA SIDO ALTERADO]\033[0m")
