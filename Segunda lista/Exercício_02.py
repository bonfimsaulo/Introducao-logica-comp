"""
02 - Faça um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.

"""

n = int(input('Digite um número:'))

# para ser par, o número precisa ser divisível por 2. Logo, o resto da divisão (%) por 2 tem que ser igual a 0

if n % 2 == 0:
    print('Este é um número par.')
else:
    print('Este é um número ímpar.')