import hmac
import hashlib
import base64

print("\n\033[35m===Simulador de HMAC===\033[0m")
print("\n\033[32m===Programa para Verificar===\033[0m")

clave=input("\n\033[31mClave Simétrica Secreta:\033[0m ")
mensaje=input("\n\033[33mMensaje:\033[0m ")
hmac_recibido=input("\n\033[34mHMAC:\033[0m ")
hmac_generado = hmac.new(bytes.fromhex(clave), mensaje.encode(), hashlib.sha256).digest()
hmac_b64= base64.b64encode(hmac_generado).decode()

if hmac.compare_digest(hmac_recibido, hmac_b64):
	print("\n\033[32m[VERIFICACIÓN EXITOSA] [+] Mensaje Auténtico\033[0m")
else:
	print("\n\033[31m[ALERTA] [-] Mensaje Modificado\033[0m")
