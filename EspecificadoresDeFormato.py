# format specifiers = {:flags} formata um valor com base em quais sinalizadores são inseridos

# .(number)f = arredondar para esse número de casas decimais (ponto fixo)
# .(number) = alocar a quantidade escolhida de espaços
# :03 = aloca e zera tantos espaços
# :< = justifica à esquerda
# :> = justifica à direita
# :^ = se alinha com o centrão
# :+ = usa um sinal de + para indicar que e positivo
# := = bota um sinaal a posição mais a esquerda
# : = coloca um espaço antes de números positivos
# :, = bota uma virgula

preço1 = 3.14159
preço2 = -987.65
preço3 = 12.34

print(f"O preço 1 é: {preço1:}")
print(f"O preço 2 é: {preço2}")
print(f"O preço 3 é: {preço3}")