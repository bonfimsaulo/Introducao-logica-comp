"""
09 - Faça um Programa que leia um número e em seguida mostre se o número é:
    inteiro ou decimal;
    positivo ou negativo;
    par ou ímpar, somente se o número for inteiro e positivo

"""

numero = float(input('Informe um número real qualquer: '))

if numero // 1 != numero and numero > 0:
    print(f'O número {numero} é decimal e positivo')
elif numero // 1 != numero and numero < 0:
    print(f'O número {numero} é decimal e negativo.')  
elif numero // 1 == numero and numero < 0:
    print(f'O número {numero} é inteiro e negativo.')  
elif numero // 1 == numero and numero > 0 and numero % 2 == 0:
    print(f'O número {numero} é inteiro, positivo e par.')  
else:
    print(f'O número {numero} é inteiro, positivo e ímpar.') 