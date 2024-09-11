# while loop = Executa algum código ENQUANTO (WHILE) alguma condição for verdadeira

# idade = int(input("Coloque sua idade: "))

# while idade < 0:
#     print("Sua idade não pode ser negativa")
#     idade = int(input("Coloque sua idade: "))

#     print(f"Você tem {idade} anos de idade")

# while nome == "":
#     print("Voce não colocou seu nome")
#     nome = input("Coloque seu nome: ")

# print(f"Olá {nome} seja bem vindo")

# comida = input("Coloque o nome da comida que você mais gosta (pressione q para sair): ")

# while not comida == "q":
#     print(f"Você gosta de {comida}")
#     comida = input("Coloque o nome de outra comida que você gosta (pressione q para sair): ")

# print("Até a proxima")

num = int(input("Coloque um número de 1 - 10: (NÃO PODE SER FRACIONARIO!)"))

while num < 1 or num > 10:
    print(f"{num} NÃO É VALIDO")
    num = int(input("Coloque um número de 1 - 10: (NÃO PODE SER FRACIONARIO!)"))

print(f"Seu número escolhido é: {num}")