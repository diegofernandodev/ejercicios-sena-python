print("========================================")
print("    SISTEMA DE CALIFICACION AMERICANO   ")
print("========================================")
print("\n")


def calificacionAmericano(numero):
    if numero < 0 or numero > 100:
        print("El numero ingresado no es valido")
    else:
        calificacion = ""
        if numero >= 90:
            calificacion = "A"
        elif numero < 90 and numero > 80:
            calificacion = "B"
        elif numero < 80 and numero > 70:
            calificacion = "C"
        elif numero < 70 and numero >= 69:
            calificacion = "D"
        elif numero < 69:
            calificacion = "F"
        print(
            f"El valor de tu calificacion es {numero}, equivalente a {calificacion}")


try:
    valor = float(input("Ingresa un numero del 0 al 100: "))
    calificacionAmericano(valor)
except:
    print("El dato ingresado no es correcto")