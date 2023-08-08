"""
12 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a) o produto do dobro do primeiro com metade do segundo .
b) a soma do triplo do primeiro com o terceiro.
c) o terceiro elevado ao cubo.
"""

num1 = int(input('Digite um número inteiro:'))
num2 = int(input('Digite um número inteiro:'))
num3 = float(input('Digite um número real:'))
op_a = (2 * num1) * (num2/2)
op_b = (3 * num1) + num3
op_c = num3 ** 3

print(f"""O produto do dobro do primeiro com metade do segundo = {op_a}
      A soma do triplo do segundo com o terceiro = {op_b}
      O terceiro elevado ao cubo = {op_c}""")