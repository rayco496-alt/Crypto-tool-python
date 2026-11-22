import os

def limpiar_pantalla():
	os.system('clear')
def menú():
	while True:
		limpiar_pantalla()
		print("\033[34m ♤♡◇♧ CAJA DE HERRAMIENTAS DE CRIPTOGRAFÍA ♤♡◇♧ \033[0m")
		print("\n\033[36m 1- Cifrado Simétrico (AES-GCM)\033[0m")
		print("\n\033[36m 2- Cifrado Híbrido (RSA + AES-GCM)\033[0m")
		print("\n\033[36m 3- Firma Digital de un Mensaje (RSA)\033[0m")
		print("\n\033[36m 4- Verificar Firma Digital (RSA)\033[0m")
		print("\n\033[36m 5- Generar HMAC\033[0m")
		print("\n\033[36m 6- Verificar HMAC\033[0m")
		print("\n\033[36m 7- Generar Pares de Llaves (RSA)\033[0m")
		print("\n\033[36m 8- Salir\033[0m")

		opcion=input("\n\033[33mOpción:\033[0m ")

		if opcion=="1":
			print("\n\033[36m 1- Cifrar\033[0m")
			print("\n\033[36m 2- Descifrar\033[0m")
			op=input("\n\033[33mOpción: \033[0m")
			if op=="1":
				operacion=os.system('python3 E_aes_gcm.py')
				if operacion != 0:
					print("\n\033[31m[ERROR] HA OCURRIDO UN PROBLEMA AL EJECUTAR EL COMANDO\033[0m")
			elif op=="2":
				operacion=os.system('python3 D_aes_gcm.py')
				if operacion != 0:
					print("\n\033[31m[ERROR] HA OCURRIDO UN PROBLEMA AL EJECUTAR EL COMANDO\033[0m")
			else:
				print("\n\033[31m[-] OPCIÓN INVÁLIDA\033[0m")
			input("Presione Enter para continuar...")
		elif opcion=="2":
			print("\n\033[36m 1- Cifrar\033[0m")
			print("\n\033[36m 2- Descifrar\033[0m")
			op=input("\n\033[33mOpción: \033[0m")
			if op=="1":
				operacion=os.system('python3 EH_aes_gcm.py')
				if operacion != 0:
					print("\n\033[31m[ERROR] HA OCURRIDO UN PROBLEMA AL EJECUTAR EL COMANDO\033[0m")
			elif op=="2":
				operacion=os.system('python3 DH_aes_gcm.py')
				if operacion != 0:
					print("\n\033[31m[ERROR] HA OCURRIDO UN PROBLEMA AL EJECUTAR EL COMANDO\033[0m")
			else:
				print("\n\033[31m[-] OPCIÓN INVÁLIDA\033[0m")
			input("Presione Enter para continuar...")
		elif opcion=="3":
			operacion=os.system('python3 firmar_mensaje.py')
			if operacion != 0:
					print("\n\033[31m[ERROR] HA OCURRIDO UN PROBLEMA AL EJECUTAR EL COMANDO\033[0m")
			input("Presione Enter para continuar...")
		elif opcion=="4":
			operacion=os.system('python3 Verificar_firma_de_mensaje.py')
			if operacion != 0:
					print("\n\033[31m[ERROR] HA OCURRIDO UN PROBLEMA AL EJECUTAR EL COMANDO\033[0m")
			input("Presione Enter para continuar...")
		elif opcion=="5":
			operacion=os.system('python3 hmac_simulador.py')
			if operacion != 0:
					print("\n\033[31m[ERROR] HA OCURRIDO UN PROBLEMA AL EJECUTAR EL COMANDO\033[0m")
			input("Presione Enter para continuar...")
		elif opcion=="6":
			operacion=os.system('python3 hmac_simulador_verificacion.py')
			if operacion != 0:
					print("\n\033[31m[ERROR] HA OCURRIDO UN PROBLEMA AL EJECUTAR EL COMANDO\033[0m")
			input("Presione Enter para continuar...")
		elif opcion=="7":
			operacion=os.system('python3 rsa_generador_claves.py')
			if operacion != 0:
					print("\n\033[31m[ERROR] HA OCURRIDO UN PROBLEMA AL EJECUTAR EL COMANDO\033[0m")
			input("Presione Enter para continuar...")
		elif opcion=="8":
			print("\n\033[33mSaliendo...\033[0m")
			break
		else:
			print("\n\033[31m[-] OPCIÓN INVÁLIDA\033[0m")
			input("Presione Enter para continuar...")

if __name__=="__main__":
	menú()
