print("========================================")
print("          SECUENCIA DE NUMEROS          ")
print("========================================")
print("\n")

try:
    numero = int(input("Ingresa un numero: "))
    print(numero)
    pregunta = input("¿Deseas imprimir el siguiente numero? si/no: ").lower()
    if pregunta == "si" or pregunta == "no":
        while pregunta == "si":
            numero += 1
            print(numero)
            pregunta = input(
                "¿Deseas imprimir el siguiente numero? si/no: ").lower()
        print("Fin.....")
    else:
        print("La respuesta ingresada no es correcta...")
except:
    print("Debes ingresar un numero entero")