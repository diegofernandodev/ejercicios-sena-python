print("========================================")
print("         MOSTRAR RANGO DE NUMEROS       ")
print("========================================")
print("\n")

numero_uno = int(input("Ingresa el numero donde inicia el rango: "))
numero_dos = int(input("Ingresa el numero donde termina el rango: "))

if numero_dos < 0:
    for i in range(numero_uno, numero_dos-1, -1):
        if i == numero_dos:
            print(i, end="")
        else:
            print(i, end=", ")
else:
    for i in range(numero_uno, numero_dos+1, +1):
        if i == numero_dos:
            print(i, end="")
        else:
            print(i, end=", ")