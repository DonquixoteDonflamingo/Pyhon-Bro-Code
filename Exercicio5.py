# Exercicio para validar a entrada do usuario
# 1. O nome do usuario não pode ter mais de 12 caracteres
# 2. O nome do usuaria não pode ter espaços
# 3. O nome do usuario não pode conter digitos

username = input("Coloque um nome: ")

if len(username) > 12:
    print("Seu nome de usuario não pode ter mais de 12 caracteres")
elif not username.find(" ") == -1:
    print("Seu nome de usuario não pode conter espaços")
elif not username.isalpha():
    print("Seu nome de usuario não pode conter digitos")
else:
    print(f"Seja Bem-Vindo {username}")