"""
14 - Faça um programa que peça o tamanho de um arquivo para download (em MB, megabytes) 
e a velocidade de um link de Internet (em Mbps, megabits por segundo), 
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos). Considere que 1 byte = 8 bits
"""
arquivo = float(input('Informe o tamanho do arquivo para download [MB]:'))
veloc_link = float(input('Informe a velocidade de um link de internet [Mbps]:'))
tempo_down = (arquivo * 8) / (veloc_link * 60) # 1byte = 8bits | 1min = 60s
print(f'O tempo aproximado de download é de {tempo_down} minutos.')