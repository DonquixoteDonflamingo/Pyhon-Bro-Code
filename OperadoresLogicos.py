# Operadores Lógicos = Avalie várias condições (or, and, not)
#                      Or = Pelo menos uma condição deve ser verdadeira
#                      And = Ambas as condições devem ser verdadeiras
#                      Not = Inverte a condição (não Falso, não Verdadeiro)

# OR
#temp = 28
#ta_chovendo = True

#if temp > 35 or temp < 0 or ta_chovendo:
#    print("O evento a céu aberto está cancelado!")
#else:
#    print("O evento à céu aberto ainda está marcado!")

# AND
temp = 33
ensolarado = False

if temp >= 28 and ensolarado:
    print("Está muito quente!")
elif temp <= 0 and ensolarado:
    print("Está muito frio lá fora!")
elif 18 >= temp >= 0 and ensolarado:
    print("Está agradavel lá fora!")
elif temp >= 28 and not ensolarado:
    print("Está muito quente!")
    print("É está nublado")
elif temp <= 0 and not ensolarado:
    print("Está muito frio lá fora!")
    print("É está nublado")
elif 18 >= temp >= 0 and not ensolarado:
    print("Está agradavel lá fora!")
    print("É está nublado")