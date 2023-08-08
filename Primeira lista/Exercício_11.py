# 11 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. Fórmula: C = 5 * ((F-32) / 9).
temp_far = float(input('Digite a temperatura [°F]:'))
temp_cels = 5 * ((temp_far - 32)/9)
print(f'{temp_far} [°F] = {temp_cels} [°C]')