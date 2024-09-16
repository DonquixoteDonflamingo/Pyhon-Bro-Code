comidas = []
precos = []
total = 0

while True:
    comida = print("Coloque uma comida para comprar: (Pressione Q para sair)")
    if comida == "q" or "Q":
        break
    else:
        preço = float(input(f"Coloque o preço de {comida}: R$"))
        comidas.append(comida)
        precos.append(preço)
