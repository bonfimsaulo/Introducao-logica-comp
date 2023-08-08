"""
05 - Faça um programa que leia dois números e mostre qual deles é maior e menor

"""

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: ')) 

if n1 > n2:
    print(f"""Maior: {n1}
Menor: {n2}""")
    
elif n2 > n1:
    print(f"""Maior: {n2}
Menor: {n1}""")
    
else:
    print('Os números são iguais.')