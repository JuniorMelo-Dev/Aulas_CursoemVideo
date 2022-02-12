# Criando estrutura de repetição 'FOR' (laço)

for c in range(1, 6):  # contagem de 1 a 5 (pois na última casa o python para)
    print(c)
print('Acabou')

for c in range(6, 0, -1):  # contagem inversa de 6 a 1 (de 1 em 1)
    print(c)
print('Acabou')

for c in range(0, 7, 2):  # contagem de 0 a 6 (de 2 em 2)
    print(c)
print('Fim')

n = int(input('Digite um número: '))
for c in range(0, n):
    print(c)
print('Fim')

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n  # s += ( é quando a variável anterior recebe ela mesma )
print('O somatório de todos os valores foi {}'.format(s))
