print("========================================")
print("           DIA DE PICO Y PLACA          ")
print("========================================")
print("\n")

try:
    placa = input("Ingresa la placa de tu vehiculo (ejm: DFE48F): ")

    placa_lista = [char for char in placa]
    if len(placa) != 6:
        print("Los datos de la placa no son correctos ")
    else:
        if int(placa_lista[4]) == 9 or int(placa_lista[4]) == 0:
            print("Tu dia de pico y placa es el dia jueves")
        elif int(placa_lista[4]) == 1 or int(placa_lista[4]) == 2:
            print("Tu dia de pico y placa es el dia viernes")
        elif int(placa_lista[4]) == 3 or int(placa_lista[4]) == 4:
            print("Tu dia de pico y placa es el dia Lunes")
        elif int(placa_lista[4]) == 5 or int(placa_lista[4]) == 6:
            print("Tu dia de pico y placa es el dia martes")
        elif int(placa_lista[4]) == 7 or int(placa_lista[4]) == 8:
            print("Tu dia de pico y placa es el dia miercoles")
except:
    print("El formato de placa que ingresaste no es valido ")