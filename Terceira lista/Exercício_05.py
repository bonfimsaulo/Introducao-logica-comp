### 05
print('Refaça o exercício da tabuada de um número que o usuário escolher, só que agora utilizando um laço For.')

n = int(input('Digite um número: '))

for c in range (1, 10 + 1):
    print(f"""{n} x {c} = {n * c}""" )