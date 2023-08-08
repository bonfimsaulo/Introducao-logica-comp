"""
21 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo 
e que calcule e mostre o comprimento da hipotenusa.
"""
cat_op = float(input('Valor do cateto oposto:'))
cat_adj = float(input('Valor do cateto adjacente:'))
hipotenusa = (cat_op ** 2 + cat_adj ** 2) ** (1/2)
print(f'A hipotenusa é {hipotenusa}')
