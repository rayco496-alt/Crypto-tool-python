from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
import base64

cifrado=input("Cifrado: ")
clave=input("\nClave: ")
nonce=input("\nNonce: ")
tag=input("\nTag: ")
archivo_clave_privada=input("\nArchivo con la Clave Privada: ")
clave_privada = RSA.import_key(open(archivo_clave_privada).read())

print("\033[35m---INICIANDO DESCIFRADO---\033[0m")

cifrador_rsa = PKCS1_OAEP.new(clave_privada)
clave_descifrada=cifrador_rsa.decrypt(base64.b64decode(clave))
descifrador = AES.new(clave_descifrada, AES.MODE_GCM, nonce=base64.b64decode(nonce))

try:
	mensaje = descifrador.decrypt_and_verify(base64.b64decode(cifrado), base64.b64decode(tag))
	print(f"\n\033[32m[EXITO] Mensaje: {mensaje.decode()}\033[0m")
except ValueError:
	print(f"\n\033[31m[ALERTA] -- [ERROR] -- [EL MENSAJE HA SIDO ALTERADO]\033[0m")
