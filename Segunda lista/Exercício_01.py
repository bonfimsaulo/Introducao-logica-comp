""" 
01 - Faça um programa que leia a velocidade de um carro. 
Se ele ultrapassar 80 km/h, mostre uma mensagem informando que ele foi multado. 
Além disso, calcule o valor da multa que irá custar R$ 70,00 por cada km passado acima do limite.

"""

veloc_carro = float(input('Velocidade:'))
multa = 70.00 * (veloc_carro - 80)

if veloc_carro > 80:
    print(f""" Você foi flagrado em uma velocidade de {veloc_carro}, acima da permitida de 80 km/h. 
          Portanto, você foi multado no valor de R$ {multa} """)
elif veloc_carro < 0:
    print('ERRO!')
else:
    print('Velocidade Permitida!')