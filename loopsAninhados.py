# nested loops = É um loop dentro de outro loop (exterior, interior) (outer, inner)
#                outer loop:
#                   inner loop:

linhas = int(input("Coloque um número de linhaa: "))
colunas = int(input("Coloque um número de colunas: "))
simb = ""

for x in range(linhas):
    for y in range(colunas):
        print(simb, end=" ")    # Se precisar de todos os números em uma linha só = end="" 
    print()