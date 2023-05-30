print("========================================")
print("     DESCOMPONER EN FACTORES PRIMOS     ")
print("========================================")
print("\n")


def descomponer_en_factores_primos(numero):
    factores_primos = []
    divisor = 2  # Comenzamos dividiendo por el primer número primo

    while divisor <= numero:
        if numero % divisor == 0:
            factores_primos.append(divisor)
            numero /= divisor
        else:
            divisor += 1

    return factores_primos


numero = int(input("Ingresa un número entero: "))
fac_primos = descomponer_en_factores_primos(numero)
print(f"Los factores primos de {numero} son {fac_primos}")