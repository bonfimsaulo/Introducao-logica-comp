"""
03 - Faça um programa que pergunte a distância de uma viagem em quilômetros.
Calcule o preço da passagem do ônibus, cobrando R$ 0,85 por cada km rodado
para viagens de até 200 km e R$ 0,57 para viagens com mais de 200 km.

"""

dist_viagem = float(input('Informe a distância da viagem em km:'))

if dist_viagem <= 200:
    preco_viagem = dist_viagem * 0.85
    print(f'O valor da passagem é de R$ {preco_viagem}.')
else:
    preco_viagem = dist_viagem * 0.57
    print(f'O valor da passarem é de R$ {preco_viagem}.')