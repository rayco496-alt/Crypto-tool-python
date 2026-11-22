from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

cifrado=input("Cifrado: ")
clave=input("\nClave: ")
nonce=input("\nNonce: ")
tag=input("\nTag: ")

print("\033[35m---INICIANDO DESCIFRADO---\033[0m")

descifrador = AES.new(bytes.fromhex(clave), AES.MODE_GCM, nonce=base64.b64decode(nonce))

try:
	mensaje = descifrador.decrypt_and_verify(base64.b64decode(cifrado), base64.b64decode(tag))
	print(f"\n\033[32m[EXITO] Mensaje: {mensaje.decode()}\033[0m")
except ValueError:
	print(f"\n\033[31m[ALERTA] -- [ERROR] -- [EL MENSAJE HA SIDO ALTERADO]\033[0m")
