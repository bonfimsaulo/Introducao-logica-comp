### 07
print('Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.')

n = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão dessa PA: '))
ultimo_termo = n + 9 * razao 

for c in range (n, ultimo_termo + razao, razao):
    pa = n + razao
    print(c)