# format specifiers = {:flags} formata um valor com base em quais sinalizadores são inseridos

# .(number)f = arredondar para esse número de casas decimais (ponto fixo)
# .(number) = alocar a quantidade escolhida de espaços
# :03 = aloca e zera tantos espaços
# :< = justifica à esquerda
# :> = justifica à direita
# :^ = se alinha com o centrão
# :+ = usa um sinal de + para indicar que e positivo
# := = bota um sinal a posição mais a esquerda
# : = coloca um espaço antes de números positivos
# :, = bota uma virgula

preço1 = 3000.14159
preço2 = -9870.65
preço3 = 1200.34

print(f"O preço 1 é: R${preço1:+,.2f}")
print(f"O preço 2 é: R${preço2:+,.2f}")
print(f"O preço 3 é: R${preço3:+,.2f}")