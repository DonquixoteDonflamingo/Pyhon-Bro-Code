# Collection (Coleção) = Única "variável" usada para armazenar vários valores
#       Lista = [] ordanada e mutavel. Pode ter duplicados
#       Conjunto = {} desordenada e imutavel, mas pode adicionar e mover. SEM NADA DUPLICADO
#       Tupla = () ordenada e imutavel. Duplicados Ok. MAIS RAPIDA

frutas = ["Maça", "laranja", "banana", "coco"] # Se for uma lista, bote o nome em plural

# É possivel inserir um valor em um index especifico
frutas.insert(0, "abacaxi")
print(frutas)
# Também da para remover algum valor de uma lista
# frutas.remove("Maça")
# Também da para acrecentar elementos a umaa lista
# frutas.append("Abacaxi")
# Listas são mutaveis
# frutas[0] = "Abacaxi"
# Para saber se um valor que você está procurando está na lista   
# print("Maça" in frutas)
# Para mostar o tamanho da lista
# print(len(frutas))
# Para mostrar os metodos de umaa lista
# print(dir(frutas))
# Para mostrar o que se pode fazer com as listas
# print(help(frutas))
# Para mostrar a lista ao contrario
# print(frutas[::-1])

# Se o nome da sua coleção for plural, seu contador será singular
# for fruta in frutas:
#     print(fruta)

# append(self, object, /) = Anexa o objeto ao final da lista.

# clear(self, /) = Remove todos os itens da lista.

# copy(self, /) = Retorna uma cópia superficial da lista.

# count(self, value, /) = Retorna o número de ocorrências de um valor.

# extend(self, iterable, /) = Estende a lista anexando elementos da iterável.

# index(self, value, start=0, stop=9223372036854775807, /) = Retorne o primeiro índice do valor.
#                                                            Gera ValueError se o valor não estiver presente.

# insert(self, index, object, /) = Insire um objeto antes do índice.

# pop(self, index=-1, /) = Remova e retorna o item no índice (último por padrão).
#                          Gera IndexError se a lista estiver vazia ou o índice estiver fora do intervalo.

# remove(self, value, /) = Remova a primeira ocorrência do valor.
#                          Gera ValueError se o valor não estiver presente.

# reverse(self, /) = Inverta *NO LUGAR*.

# sort(self, /, *, key=None, reverse=False) = Classifique a lista em ordem crescente e retorne Nenhum.
#                                             A classificação está no local (ou seja, a própria lista é modificada) e estável (ou seja, a ordem de dois elementos iguais é mantida).
#                                             Se uma função chave for fornecida, aplique-a uma vez a cada item da lista e classifique-os, em ordem crescente ou decrescente, de acordo com seus valores de função.
#                                             O sinalizador reverso pode ser configurado para classificar em ordem decrescente.