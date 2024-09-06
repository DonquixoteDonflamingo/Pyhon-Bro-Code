# If = Roda o código apenas SE alguma condição for verdadeira
# Else = faz algumaa outra coisa ate que o If seja verdadeiro

idade = int(input("Coloque a sua idade: "))

if idade >= 100:
    print("Você esta muito velho para beber e dirigir :(")
elif idade >= 18:
    print("Agora você já pode ser preso por beber E dirigir!")
elif idade < 0:
    print("Você ainda não nasceu!")
else:
    print("Você ainda não pode ser preso por beber e dirigir :(")