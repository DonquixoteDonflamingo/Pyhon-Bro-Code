import time

temp = int(input("Coloque o tempo em segundos: "))
# aqui ele basicamente está incrementando ao contrario, -1.
for x in range(temp, 0, -1):
#função sleep = Faz o progama passar uma certa quantidade de tempo "dormindo", e depois ele executa o código.
    time.sleep(1)
    segundos = x % 60
    minutos = int(x / 60) % 60
    horas = int(x / 3600)
    print(f"{horas:02}:{minutos:02}:{segundos:02}")

print("SEU TEMPO ACABOU!")