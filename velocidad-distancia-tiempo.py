print("========================================")
print("      VELOCIDAD = DISTANCIA/TIEMPO      ")
print("========================================")
print("\n")


def velocidad(distancia, tiempo):
    velocidad = distancia/tiempo
    return velocidad


try:
    distancia = float(input("Ingresa la distancia: "))

    if distancia > 20 and distancia < 35:
        tiempo = float(input("Ingresa el valor del tiempo: "))
        new_velocidad = velocidad(distancia, tiempo)
        print(f"La velocidad es {new_velocidad} km/h")
    else:
        print("Fin...")
except:
    print("El tipo de dato ingresado no es valido")