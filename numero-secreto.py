import random
print("========================================")
print("        NUMERO ALEATORIO SECRETO        ")
print("========================================")
print("\n")
num_final = int(input("Ingresa el numero final del rango: "))
num_random = random.randrange(1, num_final)

resultado_ingresado = int(input(f"Ingresa un numero del 1 al {num_final}: "))

while resultado_ingresado != num_random:
    if resultado_ingresado < num_random:
        print("El numero que ingresaste es menor al numero que debes acertar.")
    else:
        print("El numero que ingresaste es mayor al numero que debes acertar.")

    resultado_ingresado = int(
        input(f"Ingresa un numero del 1 al {num_final}: "))

print(f"¡¡¡Acertaste!!! el numero aleatoreo es {num_random}")