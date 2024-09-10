# indexing = acessando elementos de uma sequência usando [] (operador de indexação)
#            [start : and : step]

num_cartao = "1234-5678-9012-3456"

# Permite escolher qual parte daquela string você quer acessar
# print(num_cartao[:4])
# print(num_cartao[5:9])
# print(num_cartao[5:])
# print(num_cartao[-2])
# print(num_cartao[::2]) step

# ult_4_digit = num_cartao[-4:]

# print(f"XXXX-XXXX-XXXX-{ult_4_digit}")
# Se colocar -1 no lugar do step, essa função reverterá a string
num_cartao = num_cartao[::-1]
print(num_cartao)