# Exércicio 2 = Programa de carrinho de compras

itens = input("Que item você gostaria de comprar?: ")
preço = float(input("Qual é o preço?: "))
quantidade = int(input("Quantas gramas você gostaria de comprar?: "))

total = preço * quantidade

print(f"Deu exatamente {total}R$ de {itens}")