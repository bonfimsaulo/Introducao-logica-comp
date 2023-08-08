#### 03
print("""Crie um programa que mostre na tela a soma de todos os números pares que estão no intervalo entre 1 e 50.""")

soma_pares = 0

for c in range(2, 50 + 2, 2):
    soma_pares += c
print(f'A soma dos números pares de 1 a 50 é {soma_pares}')