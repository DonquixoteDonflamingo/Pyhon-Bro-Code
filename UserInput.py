# input () = Uma função que solicita ao usuário a inserção de dados
#            Retorna os dados inseridos como uma string

nome = input("Qual e o seu nome?: ")
idade = int(input("Quantos anos você tem?: "))

# Como os dados recebidos serão uma string, deve-se usar o typecasting para poder fazer as contas
idade += 1

print(f"Olá {nome}!")
print("DIA 15 SERÁ SEU ANIVERSÁRIO!")
print(f"Você terá {idade} anos de idade")