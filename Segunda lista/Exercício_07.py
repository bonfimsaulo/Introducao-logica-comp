"""
07 - Desenvolva um programa que leia o comprimento de três retas
e mostre se elas podem ou não formar um triângulo. 

"""    

lado1 = int(input('Digite o comprimento da primeira reta:'))
lado2 = int(input('Digite o comprimento da segunda reta:'))
lado3 = int(input('Digite o comprimento da terceira reta:'))

if lado1 > abs(lado2 - lado3) and lado1 < lado2 + lado3 and lado2 > abs(lado1 - lado3) and lado2 < lado1 + lado3 and lado3 > abs(lado1 - lado2) and lado3 < lado1 + lado2:
    print(f'Os lados {lado1} cm, {lado2} cm e {lado3} cm formam um triângulo.')
else:
    print(f'Os lados {lado1} cm, {lado2} cm e {lado3} cm não formam um triângulo.')