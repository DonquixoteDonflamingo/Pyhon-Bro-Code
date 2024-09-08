#Conversor de temperatura

unidade = input("A temperatura está em Celsius ou Fahrenheit?(C/F): ")
temp = float(input("Coloque o valor da temperatura: "))

if unidade == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"A temperatura em Fahrenheit é: {temp}°F")
elif unidade == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"A temperatura em Celsius é: {temp}°C")
else:
    print(f"{unidade} Não é uma medida valida!")