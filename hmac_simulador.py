import hmac
import hashlib
import base64

print("\n\033[35m===Simulador de HMAC===\033[0m")
clave=input("\n\033[31mClave Simétrica Secreta:\033[0m ")
mensaje=input("\n\033[33mMensaje:\033[0m ")

hmac_generado = hmac.new(bytes.fromhex(clave), mensaje.encode(), hashlib.sha256).digest()
hmac_b64= base64.b64encode(hmac_generado).decode()
print(f"\n\033[34mHMAC: {hmac_b64} (base64)\033[0m")

