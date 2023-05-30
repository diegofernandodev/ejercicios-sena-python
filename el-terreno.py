print("========================================")
print("                 EL TERRENO             ")
print("========================================")
print("\n")


def areaTriangulo(base, altura):
    area = base * altura / 2
    return area


def areaRectangulo(base, altura):
    area = base * altura
    return area


try:
    base = float(input("Ingrese la base: "))
    altura = float(input("Ingrese la altura: "))
    if base <= 0 or altura <= 0:
        print("El valor ingresado debe ser mayor a cero")
    else:
        a_triangulo = areaTriangulo(base, altura)
        a_rectangulo = areaRectangulo(base, altura)

        print(
            f"El area del triangulo es {a_triangulo} y el area del rectangulo es {a_rectangulo}")

        if a_triangulo > a_rectangulo:

            print(f"El terreno mas grande es el Triangular {a_triangulo}")
        else:
            print(f"El terreno mas grande es el rectangular {a_rectangulo}")
except:
    print(f"Los datos ingresados deben ser numericos")
