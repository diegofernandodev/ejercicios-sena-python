print("========================================")
print("          FACTORIAL DE UN NUMERO        ")
print("========================================")
print("\n")

numero = int(input("Ingresa un numero: "))
imprim_numero = numero
factorial = 1
for j in range(1, numero+1, 1):
    factorial *= j
    print(factorial, end=" ")
print("\n"f"El factorial de {imprim_numero} es {factorial}")