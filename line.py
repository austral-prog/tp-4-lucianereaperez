import math
def line():
    coefA = float(input("Ingrese el coeficiente A:"))
    coefB = float(input("Ingrese el coeficiente B:"))
    coefx1 = float(input("Ingrese el coeficiente X1:"))
    coefx2 = float(input("Ingrese el coeficiente X2:"))
    y1 = (coefA*coefx1) + coefB
    y2 = (coefA*coefx2) + coefB
    P1 = [coefx1, y1]
    P2 = [coefx2, y2]
    print(f"El coeficiente A de su ecuación de la recta es: {coefA}")
    print(f"El coeficiente B de su ecuación de la recta es: {coefB}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {coefx1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {coefx2}")
    print("")
    print("Para la siguiente ecuación:")
    print(f"\tY = {coefA}X + {coefB}")
    print("")
    print("Dados los siguientes puntos:")
    print(f"\tP1 ({coefx1}, {y1})")
    print(f"\tP2 ({coefx2}, {y2})")
    print("")
    distance = math.dist(P1, P2)
    print(f"La distancia entre ellos es: {distance}")
