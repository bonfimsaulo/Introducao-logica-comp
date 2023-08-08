# 09 - Faça um Programa que calcule a área de um círculo, em centímetros, em seguida mostre o dobro desta área para o usuário.
raio_circ = float(input('Informe o valor do raio da circunferência:'))
pi = 3
area_circ = pi * raio_circ ** 2
area_dobro = 2 * area_circ
print(f'O dobro da área da circunferência de raio {raio_circ} [cm] = {area_dobro} [cm²]')