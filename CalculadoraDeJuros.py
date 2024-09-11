investimento = 0
taxa = 0
tempo = 0

while investimento <= 0:
    investimento = float(input("Coloque a quantidade inicial de investimento: "))
    if investimento <= 0:
        print("O investimento inicial não pode ser menor ou igual à zero!")

while taxa <= 0:
    taxa = float(input("Coloque a taxa de juros inicial: "))
    if taxa <= 0:
        print("A taxa de juros inicial não pode ser menor ou igual à zero!")

while tempo <= 0:
    tempo = int(input("Coloque o tempo em anos que gostaria que resgatar seu investimento: "))
    if tempo <= 0:
        print("O tempo não pode ser menor ou igual à zero!")

total = investimento * pow((1 + taxa / 100), tempo)

print(f"O seu saldo após {tempo} ano/s será: R${total:.2f}")