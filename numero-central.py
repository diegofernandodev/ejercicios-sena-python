print("========================================")
print("      CUAL NUMERO DE 3 ES EL CENTRAL    ")
print("========================================")
print("\n")


def numeroCentral(valor_uno, valor_dos, valor_tres):
    if valor_uno <= valor_dos <= valor_tres or valor_tres <= valor_dos <= valor_uno:
        print(f"{valor_dos} es el numero medio")
    elif valor_dos <= valor_uno <= valor_tres or valor_tres <= valor_uno <= valor_dos:
        print(f"{valor_uno} es el numero medio")
    elif valor_uno <= valor_tres <= valor_dos or valor_dos <= valor_tres <= valor_uno:
        print(f"{valor_tres} es el numero medio")


vr_uno = int(input("Ingresa el primer numero: "))
vr_dos = int(input("Ingresa el segundo numero: "))
vr_tres = int(input("Ingresa el tercer numero: "))

numeroCentral(vr_uno, vr_dos, vr_tres)