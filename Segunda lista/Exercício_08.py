"""
08 - Faça um programa que peça um valor e mostre na tela se ele é posivito ou negativo.

"""

num = float(input('Digite um número:'))

if num > 0:
    print(f'O número {num} é positivo.')
elif num == 0:
    print('Zero é um número neutro.')
else:
    print(f'O número {num} é negativo.')