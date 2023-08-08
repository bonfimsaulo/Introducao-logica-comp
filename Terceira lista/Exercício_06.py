### 06
print("""Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares e 
quantos números pares foram informados. Se o valor digitado for ímpar, desconsidere-o na soma.""")

soma = 0
pares = 0

for c in range (1, 6 + 1):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        pares += 1
        soma += c
print(f"""Total de pares: {pares}
Soma: {soma}""")