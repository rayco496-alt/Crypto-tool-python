from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
import base64

mensaje = input("Mensaje: ")
clave = get_random_bytes(32)
print(f"\nLlave Aleatoria Generada para ese mensaje: {clave.hex()}  (32-hex)")

archivo_clave_pública=input("Archivo de Clave Pública: ")
clave_pública=RSA.import_key(open(archivo_clave_pública).read())

cifrador = AES.new(clave, AES.MODE_GCM)

cifrado, tag = cifrador.encrypt_and_digest(mensaje.encode())

nonce = cifrador.nonce

cifrador_RSA = PKCS1_OAEP.new(clave_pública)
clave_AES_cifrada = cifrador_RSA.encrypt(clave)

print("\033[35m---CIFRADO EXITOSO---\033[0m")
print(f"\n\033[31mNONCE: {base64.b64encode(nonce).decode()} (base64)\033[0m")
print(f"\n\033[33mMensaje Cifrado: {base64.b64encode(cifrado).decode()} (base64)\033[0m")
print(f"\n\033[32mTAG DE INTEGRIDAD: {base64.b64encode(tag).decode()} (base64)\033[0m")
print(f"\n\033[31mCLAVE CIFRADA: {base64.b64encode(clave_AES_cifrada).decode()} (base64)\033[0m\n")
