"""
06 - Faça um algoritmo que pergunte o salário de um funcionário e calcule o novo salário com aumento.
- Para salários de até R$ 1320,00, o aumento será de 15% 
- Para salários superiores a R$ 1320,00 o aumento será de 10%

""" 

salario = float(input('Informe seu salário: R$ '))

if salario > 1320:
    salario = salario * 1.10
    salario = round(salario, 2)
    print(f'Seu salário de R$ {salario} teve um aumento de 10 % e o novo valor será de R$ {salario}. ')
else:
    salario *= 1.15
    salario = round(salario, 2)
    print(f'Seu salário de R$ {salario} teve um aumento de 15 % e o novo valor será de R$ {salario}. ')