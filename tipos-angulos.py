print("========================================")
print("             TIPOS DE ANGULOS           ")
print("========================================")
print("\n")

try:
    angulo = int(input("Ingresa un angulo en grados: "))

    if angulo == 90:
        print(f"El angulo de {angulo} grados es recto")
    elif angulo < 90:
        print(f"El angulo de {angulo} grados es agudo")
    elif angulo > 90:
        print(f"El angulo de {angulo} grados es Optuso")
except:
    print("El tipo de valor ingresado no es correcto")