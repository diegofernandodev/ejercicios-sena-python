print("========================================")
print("           DIA DE PICO Y PLACA          ")
print("========================================")
print("\n")

import re

placa = input("Ingresa la placa de tu vehiculo: ")
placa = placa.upper()  # Convertir la placa a mayúsculas
# Verificar el formato de la placa utilizando una expresión regular
if not re.match(r'^[A-Z]{3}\d{3}$', placa) and not re.match(r'^[A-Z]{3}\d{2}[A-Z]$', placa):
    print("La placa ingresada no es válida.")
else:
    if len(placa) == 6:
        if placa[5].isdigit():
            ultimo_digito = placa[-1]
        else:
            ultimo_digito = placa[-2]

        if ultimo_digito in ["1", "2"]:
            print("Tienes pico y placa el día lunes")
        elif ultimo_digito in ["3", "4"]:
            print("Tienes pico y placa el día martes")
        elif ultimo_digito in ["5", "6"]:
            print("Tienes pico y placa el día miércoles")
        elif ultimo_digito in ["7", "8"]:
            print("Tienes pico y placa el día jueves")
        elif ultimo_digito in ["9", "0"]:
            print("Tienes pico y placa el día viernes")