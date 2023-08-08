# 08 - Faça um Programa que peça o raio de um círculo, em centímetros, calcule e mostre sua área. Considere pi = 3
raio_circ = float(input('Informe o valor do raio da circunferência:'))
pi = 3
area_circ = pi * raio_circ ** 2
print(f'A área da circunferência de raio {raio_circ} [cm] = {area_circ} [cm²]')