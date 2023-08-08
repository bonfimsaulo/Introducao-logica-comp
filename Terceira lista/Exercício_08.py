### 08
print("""Faça um programa que leia um número positivo e diga se ele é ou não um número primo. 
O programa deverá mostrar quantas vezes o número foi divisível.""")

n = int(input('Digite um numero: '))

totaldiv = 0

for c in range(1 , n + 1):
    if n % c == 0:
        totaldiv += 1
    
if totaldiv == 2:
    print(f'{n} é primo, pois é divisível por {totaldiv} valores (1 e ele mesmo).')
else:
    print(f'{n} não é primo, sendo divisível por {totaldiv} valor[es].')