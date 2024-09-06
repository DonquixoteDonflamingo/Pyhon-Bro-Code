# Typecasting = O processo de conversão de uma variável de um tipo de dados para outro
#               str(), int(), float(), bool()
#               É util para checar se o usuário não colocou algum dado como o nome ou cpf.

nome = ""
idade = 19
nota = 4.5
e_estudante = True

#Você pode obter qual tipo de dados esta em uma variável usando a função type()
# print(type(nome))

#nota = int(nota)
#idade = float(idade)

#idade = str(idade)
#idade += "1"

nome = bool(nome)

print(nome)