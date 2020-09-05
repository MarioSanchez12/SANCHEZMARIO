es_primo = True
numero_es_primo = int(input("Introduce un número para comprobar la raiz cuadrada: "))
for num in range(2, numero_es_primo):
	if numero_es_primo % num == 0:
		es_primo = False
if es_primo:
	print("Es raiz cudrada")
else:
	print("No es raiz cuadrada")
