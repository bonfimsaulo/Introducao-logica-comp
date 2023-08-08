"""
04 - Faça um programa que leia um ano qualquer e mostre se ele é ou não bissexto.

"""
# Condições para ser considerado ano bissexto:
# Condição 1: Ser múltiplo de 4 e não ser múltiplo de 100.
# Condição 2: Ser múltiplo de 400.

ano = int(input('Informe um ano qualquer:'))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 ==0 ):
    print(f'O ano de {ano} é um ano bissexto.')
else:
    print(f'O ano de {ano} não é um ano bissexto.')