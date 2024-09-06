#Variável - Um contêiner para um valor (inteiro, string, float, booleano)
#           Uma variável se comporta como se fosse o valor que ela contém

#Strings
primeiro_nome = "Gugu"
comida = "Pizza"
email = "GUGU123@fake.com"

print(primeiro_nome)
print(f"Ola {primeiro_nome}")     #Para usar uma variável junto com texto deve-se usar uma f-string
print(f"Voce gosta de {comida}")   #F- String = Comece uma string com F ou f antes das aspas de abertura.
print(f"Este e seu email: {email}") # Dentro desta string,
                                     #você pode escrever uma expressão Python entre caracteres { e } que pode se referir a variáveis ​​ou valores literais.
#Inteiros (Não coloque números entre "" pois serão considerados uma string)
idade = 19
quantidade = 3
num_de_estudantes = 45
#Não se pode fazer operações aritméticas com strings

print(f"Voce tem: {idade} anos")
print(f"Voce comprou {quantidade} produtos em nossa loja")
print(f"Sua classe tem {num_de_estudantes} alunos")

#Floats tem uma parte decimal (.000)
preço = 10.99
notas = 8.74
distancia = 5.8

print(f"O preco de suas compras {primeiro_nome} e de: R${preço}")
print(f"Sua nota neste semestre e: {notas}")
print(f"Voce andou {distancia}KMs")

#Boleanos
e_estudande = False

if e_estudande:
    print("Voce e um estudante em nossa escola!")
else:
    print("Voce nao e um estudante em nossa escola")