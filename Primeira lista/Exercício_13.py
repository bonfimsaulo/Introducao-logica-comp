"""
 13 - Tendo como dados de entrada a altura de uma pessoa, em centímetros, 
 construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: 
 (72.7*altura em metros) - 58
"""

altura = float(input('Informe a altura em centímetros [cm]:'))
altura_metros = altura / 100
peso_ideal = (72.7 * altura_metros) - 58
print(f'O peso ideal para uma pessoa de {altura_metros} [m] é {peso_ideal} [kg]')