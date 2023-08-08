# 07 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
preco_produto = float(input('Informe o preço do produto:'))
preco_desconto = preco_produto * 0.95
print(f'O novo preço do produto de R${preco_produto} com 5% de desconto é de R${preco_desconto} ')