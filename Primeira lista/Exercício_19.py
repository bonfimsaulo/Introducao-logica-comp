""" 
19 - Faça um algoritmo que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias que ele ficou com o veículo. 
Calcule o preço a pagar pelo aluguel, sabendo que o carro custa R$100 por dia e R$0,75 por km rodado.
"""
km_rodado = float(input('Informe a quilometragem percorrida [km]:'))
tempo_alug = int(input('Informe o tempo de aluguel em dias:'))
preco_aluguel = 0.75 * km_rodado + 100 * tempo_alug
print(f'O valor do aluguel é de R${preco_aluguel}.')