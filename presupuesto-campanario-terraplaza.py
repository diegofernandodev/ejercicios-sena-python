print("========================================")
print("     PRESUPUESTO CAMAPNARIO-TERRAPALZA  ")
print("========================================")
print("\n")


def calcularPresupuesto(presupuesto, valor_uno, valor_dos):
    resultado = presupuesto - (valor_uno + valor_dos)
    return resultado


try:
    presupuesto = int(input("Ingresa el valor de tu presupuesto: "))

    for i in range(0, 2, 1):
        lugar = input("Ingresa el lugar " + str(i+1) + ": ")
        valor_uno = int(input("Ingresa el valor del transporte: "))
        valor_dos = int(input("Ingresa el valor de otros gastos: "))
        if i == 0:
            lugar_uno = lugar
            respuesta_uno = calcularPresupuesto(
                presupuesto, valor_uno, valor_dos)
        else:
            lugar_dos = lugar
            respuesta_dos = calcularPresupuesto(
                presupuesto, valor_uno, valor_dos)
        print("\n")
    if respuesta_uno < 0 or respuesta_dos < 0:
        print("El valor total de los gastos es mayor a tu presupuesto")
    else:
        if respuesta_uno > respuesta_dos:
            print("\nSi vas a ", lugar_uno, " gastaras ", respuesta_uno -
                  respuesta_dos, " menos que si vas a ", lugar_dos, " por lo tanto es el lugar mas favorable")
        else:
            print("\nSi vas a ", lugar_dos, " gastaras ", respuesta_dos -
                  respuesta_uno, " menos que si vas a ", lugar_uno, " por lo tanto es el lugar mas favorable")
except:
    print("El dato ingresado no es valido")