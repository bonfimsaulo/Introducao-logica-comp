""" 16 - Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00. Informe ao usuário a quantidade de latas de tinta a serem compradas e o preço total.
"""
area_pintura = float(input('Informe o total ta área a ser pintada [m²]:'))

# 1 litro de tinta para cada 3m² | latas de 18 litros - R$80,00 

litros_usados = area_pintura / 3

if litros_usados % 18 > 0:
    total_latas = (litros_usados // 18) + 1
    preco_total = total_latas * 80
    print(f'Você precisará de comprar {total_latas} de latas no valor de R$ {preco_total}.')
else:
    total_latas = litros_usados / 18 
    preco_total = total_latas * 80
    print(f'Você precisará de comprar {total_latas} de latas no valor de R$ {preco_total}.')