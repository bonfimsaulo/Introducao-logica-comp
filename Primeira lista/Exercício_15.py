"""
15 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
a)salário bruto.
b)quanto pagou ao INSS.
c)quanto pagou ao sindicato.
d)o salário líquido.
e)calcule os descontos e o salário líquido, conforme a tabela abaixo:
f)+ Salário Bruto : R$
g)- IR (11%) : R$
h)- INSS (8%) : R$
i)- Sindicato ( 5%) : R$
j)= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
"""

valor_h = float(input('Digite o quanto ganha por hora trabalhada:'))
horas_trab = float(input('Digite o número de horas trabalhadas no mês:'))
salario_bruto = valor_h * horas_trab
desc_ir = salario_bruto * 0.11 # 11% desconto
desc_inss = salario_bruto * 0.08 # 8% desconto
desc_sind = salario_bruto * 0.05 # 5% desconto
salario_liquido = salario_bruto - (desc_ir + desc_inss + desc_sind)
print(f"""Salário Bruto: R$ {salario_bruto}
Desconto do IR [11%]: R$ {desc_ir}
Desconto do INSS [8%]: R$ {desc_inss}
Desconto do Sindicato [5%]: R$ {desc_sind}
Salário Líquido: R$ {salario_liquido}""")