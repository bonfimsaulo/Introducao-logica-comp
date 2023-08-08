# 18 - Solicitar a idade de uma pessoa em dias e informar na tela a idade em anos, meses e dias.
idade_dias = int(input('Informe sua idade em número de dias:'))

# considerando 1 ano = 365 dias

idade_a = idade_dias / 365 
id_a = int(idade_a)         # id_a -> parte inteira 'anos'

idade_m = (idade_a - id_a) * 12
id_m = int(idade_m)         # id_m -> parte inteira 'meses'

idade_d = (idade_m - id_m) * 30
id_d = int(idade_d)         # id_d -> parte inteira 'dias'

if idade_d - id_d >= 0.5:
    dia = id_d + 1
    print(f'{idade_dias} dias = {id_a} ano(s), {id_m} mês(es) e {dia} dia(s).')
else:
    dia = id_d
    print(f'{idade_dias} dias = {id_a} ano(s), {id_m} mês(es) e {dia} dia(s).')