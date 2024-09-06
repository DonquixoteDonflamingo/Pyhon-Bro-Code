# Um calculadora em Python

operador = input("Coloque um operador (+, -, *, /): ")
num1 = float(input("Coloque o primeiro número: "))
num2 = float(input("Coloque o segundo número: "))

# pass = Para passar para a segunda opçaõ
if operador == "+":
    resultado = num1 + num2
    print(resultado)
elif operador == "-":
    resultado = num1 - num2
    print(resultado)
elif operador == "*":
    resultado = num1 * num2
    print(resultado)
elif operador == "/":
    resultado = num1 / num2
    print(resultado)
else:
    print("Este não é um operador válido!")