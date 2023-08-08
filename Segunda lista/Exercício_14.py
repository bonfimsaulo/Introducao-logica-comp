"""
14 - Faça um programa que faça 5 perguntas de sim ou não para uma pessoa sobre um crime. As perguntas são:
"Fez a matrícula na Infinity?"
"Está treinando programação além da sala de aula?"
"Fez o teste de lógica?"
"Entrega as atividades em dia?"
"Tá aprendendo a programar pelos dedos?" 

O programa deve no final emitir uma classificação sobre a participação da pessoa no aprendizado de Python. 
Se a pessoa responder positivamente a mais de 3 questões ela deve ser classificada como 
"Está no caminho certo para ser um excelente programador". 
Caso contrário, ele será classificado como "Precisa se dedicar mais.".

"""

pergunta1 = input('Fez a matrícula na Infinity? ')
p1 = pergunta1.lower()
pergunta2 = input('Está treinando programação além da sala de aula? ')
p2 = pergunta2.lower()
pergunta3 = input('Fez o teste de lógica? ')
p3 = pergunta3.lower()
pergunta4 = input('Entrega as atividades em dia? ')
p4 = pergunta4.lower()
pergunta5 = input('Está aprendendo a programar pelos dedos? ')
p5 = pergunta5.lower()

if p1 == 'sim' and p2 == 'sim' and p3 == 'sim' and p4 == 'sim' and p5 == 'sim':
    print('Está no caminho certo para ser um excelente programador.')
elif (p1 == 'não' or p1 == 'nao') and p2 == 'sim' and p3 == 'sim' and p4 == 'sim' and p5 == 'sim':
    print('Está no caminho certo para ser um excelente programador.')
elif p1 == 'sim' and (p2 == 'não' or p2 == 'nao') and p3 == 'sim' and p4 == 'sim' and p5 == 'sim':
    print('Está no caminho certo para ser um excelente programador.')
elif p1 == 'sim' and p2 == 'sim' and (p3 == 'não' or p3 == 'nao') and p4 == 'sim' and p5 == 'sim':
    print('Está no caminho certo para ser um excelente programador.')
elif p1 == 'sim' and p2 == 'sim' and p3 == 'sim' and (p4 == 'não' or p4 == 'nao') and p5 == 'sim':
    print('Está no caminho certo para ser um excelente programador.')
elif p1 == 'sim' and p2 == 'sim' and p3 == 'sim' and p4 == 'sim' and (p5 == 'não' or p5 == 'nao'):
    print('Está no caminho certo para ser um excelente programador.')
else:
    print('Precisa se dedicar mais.')