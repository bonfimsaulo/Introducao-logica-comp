"""
17 - Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em galões de 18 litros, 
que custam R$ 80,00 ou em latinhas de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 2 situações:
a) Comprar apenas latas de 18 litros;
b) Comprar apenas galões de 3,6 litros;
"""

area_p = float(input('Informe o total ta área a ser pintada [m²]:'))

# 1 litro de tinta para cada 6m² | galão de 18 litros - R$80,00 | latinhas de 3,6 litros - R$25,00 

lit_usados = area_p / 6

if lit_usados % 18 > 0:
    galoes = (lit_usados // 18) + 1
    preco_gal = galoes * 80
else:
    galoes = lit_usados / 18
    preco_gal = galoes * 80

if lit_usados % 3.6 > 0:
    latinhas = (lit_usados // 3.6) + 1
    preco_latinha = latinhas * 25
else:
    latinhas = lit_usados / 3.6
    preco_latinha = latinhas * 25

print(f'Você precisará de comprar {galoes} galões de tinta no valor de R${preco_gal} ou {latinhas} latinhas no valor de R${preco_latinha}.')