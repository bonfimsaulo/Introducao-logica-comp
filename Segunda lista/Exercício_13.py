"""
13 - Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool - R$ 3,80 por litro
    até 20 litros, desconto de 3% por litro
    acima de 20 litros, desconto de 5% por litro
Gasolina R$ 4,70 por litro
    até 20 litros, desconto de 4% por litro
    acima de 20 litros, desconto de 6% por litro 
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível 
(codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente. 

"""

combustivel = input('Informe o combústivel para abastecimento, [A]lcool ou [G]asolina: ')
litros = float(input('Informe quantos litros para abastecimento: '))
comb = combustivel.lower()

if comb == 'a' and litros <= 20:
    preco_alc = litros * 3.80 * 0.97
    preco_alc = round(preco_alc, 2)
    print(f'O total a ser pago por {litros} litros de álcool é R$ {preco_alc}.')

elif comb == 'a' and litros > 20:
    preco_alc = litros * 3.80 * 0.95
    preco_alc = round(preco_alc, 2)
    print(f'O total a ser pago por {litros} litros de álcool é R$ {preco_alc}.')

elif comb == 'g' and litros <= 20:
    preco_gas = litros * 4.70 * 0.96
    preco_gas = round(preco_gas, 2)
    print(f'O total a ser pago por {litros} litros de gasolina é R$ {preco_gas}')

elif comb == 'g'and litros > 20:
    preco_gas = litros * 4.70 * 0.94
    preco_gas = round(preco_gas, 2)
    print(f'O total a ser pago por {litros} litros de gasolina é R$ {preco_gas}')
    
else:
    print('Dado inválido informado.')