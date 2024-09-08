# Expressão Condicional = Um atalho de uma linha para instrução if-else (operação ternária)
#                         Imprimir ou avaliar um dos dois valores com base em uma condição
#                         X if condição else Y

num = 5
a = 6
b = 7
max_num = a if a > b else b
idade = 19
temperatura = 0
user_role = "AAAAAAA"

# print("O Número é Positivo" if num > 0 else "O Número é Negativo")
# resultado = "Par" if num % 2 == 0 else "Impar"
# status = "Adulto" if idade >= 18 else "Criança"
# clima = "Quente!" if temperatura > 18 else "Frio"

nivel_de_acesso = "Acesso garantido" if user_role == "adm" else "ACESSO NEGADO!"

print(nivel_de_acesso)