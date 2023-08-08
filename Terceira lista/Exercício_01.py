### 01
print("""1 - Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, 
indo de 10 até 0 e após o 0 mostre “BOOOM!”""")

from time import sleep

for cont in range(10, -1, -1 ):
    print(cont)
    sleep(1)
print('BOOOM!')