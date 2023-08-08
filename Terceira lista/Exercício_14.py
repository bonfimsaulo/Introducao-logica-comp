### 14
print("""O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. 
Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém 
o número de itens que o cliente comprou e ao lado o valor da conta. 
Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. 
Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos.""")
print('---------------------------------')

print("""     LOJA QUASE DOIS
    Tabela de preços:""")

print('---------------------------------')
print('Ítem                        R$')
item = 0
preco = 0
n = 50
condicao = True
while condicao:
    if item < n:
        preco += 1.99
        preco = round(preco, 2)
        item += 1
        print(f'{item}             -            {preco}')
    else:
        condicao = False