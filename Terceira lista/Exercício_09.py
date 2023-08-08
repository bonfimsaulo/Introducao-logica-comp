### 09
print("""Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.""")

maioridade = 0
menoridade = 0

for c in range (1, 7 + 1):
    n = int(input('Informe o ano de nascimento: '))
    
    if 2023 - n >= 18:
        maioridade += 1
    else:
        menoridade += 1

print(f"""{maioridade} pessoas atingiram a maioridade enquanto que
{menoridade} pessoas ainda não.""")