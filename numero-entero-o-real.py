print("========================================")
print("DETERMINAR SI UN NUMERO ES ENTERO O REAL")
print("========================================")
print("\n")

numero = input("Ingresa un numero: ")

if "." in numero:
    print(f"El numero {numero} ingresado es un real")
elif numero.isdigit():
    numero = int(numero)
    print(f"El numero {numero} ingresado es un entero")
else:
    print("Dato ingresado no es valido")