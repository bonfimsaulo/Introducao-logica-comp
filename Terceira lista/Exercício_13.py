### 13
print("""Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.""")

eleitores = int(input('Informe o total de eleitores: '))
pop_ele = 0
a = 0
b = 0
c = 0
nulo = 0


condicao = True

while condicao:
   
    if eleitores > pop_ele:
        voto = input(("""Vote em um dos candidatos abaixo: 
                [A]
                [B]
                [C]
                Voto:  """)).lower()
        if voto == 'a':
            a += 1
            pop_ele += 1
        elif voto == 'b':
            b += 1
            pop_ele += 1
        elif voto == 'c':
            c += 1
            pop_ele += 1
        else:
            nulo += 1
            pop_ele += 1
    else:
        condicao = False

print(f"""Resultado das eleições:
    Candidato A: {a}
    Candidato B: {b}
    Candidato C: {c}
    votos nulos: {nulo}
    Total de votos: {eleitores}""")

if a > b and a > c:
    print('O candidato A é o vencedor!')
elif b > a and b > c:
    print('O candidato B é o vencedor!')
elif c > a and c > b:
    print('O candidato C é o vencedor!')