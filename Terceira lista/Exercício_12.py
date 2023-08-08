### 12
print('Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário')

n = int(input('Digite um número inteiro: '))
fator = n

for c in range (n - 1, 0, -1):
    fator *= c
print(f'{n}! = {fator}')