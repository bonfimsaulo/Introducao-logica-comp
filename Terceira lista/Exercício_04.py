### 04
print("""Faça um programa que peça 10 números inteiros, 
calcule e mostre a quantidade de números pares e a quantidade de números impares.""")

qtd_pares = 0
qtd_impares = 0

for c in range(1, 10 + 1):
    n = int(input('Digite um número inteiro: '))
    
    if n % 2 == 0:
        qtd_pares += 1
    else:
        qtd_impares += 1

print(f"""Total de pares: {qtd_pares}
Total de ímpares: {qtd_impares}""")