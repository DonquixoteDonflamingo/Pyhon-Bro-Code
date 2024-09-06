import math

a = float(input("Coloque o tamanho do lado A: "))
b = float(input("Coloque o tamanho do lado B: "))

c = math.sqrt((pow(a, 2) + pow(b, 2)))

print(f"O Tamanho do lado C deste triangulo é de: {round(c)}cm")