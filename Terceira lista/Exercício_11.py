### 11
print("""Faça um programa que conte de 1 até o número do usuário, determine o menor valor, o maior valor e a soma dos valores. 
Faça que o programa receba apenas números entre 0 e 1000.""")

condicao = True

while condicao:
    n = int(input('Digite um número: '))

    if n <= 0 or n > 1000:
        print('Entrada inválida. Informe um número entre 1 e 1000: ')
    else:
        condicao = False
        
for c in range (1, n + 1):
    print(c)