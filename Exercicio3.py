# Conversor de peso em python

Peso = float(input("Coloque seu peso: "))
unidade = input("Está em Kilos ou Libras ?(Digite K ou L: )")

if unidade == "K":
    Peso *= 2.205
    unidade = "Lbs."
    print(f"Seu peso é: {round(Peso, 1)} {unidade}")
elif unidade == "L":
    Peso /= 2.205
    unidade = "Kgs"
    print(f"Seu peso é: {round(Peso, 1)} {unidade}")
else:
    print(f"{unidade} Não é uma medida de peso valida!")