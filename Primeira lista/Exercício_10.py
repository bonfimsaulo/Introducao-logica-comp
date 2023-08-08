# 10 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
valor_hora = float(input('Digite o quanto ganha por hora trabalhada:'))
numero_horas = float(input('Digite o número de horas trabalhadas no mês:'))
salario = valor_hora * numero_horas
print(f'O salário do mês é de R${salario}')