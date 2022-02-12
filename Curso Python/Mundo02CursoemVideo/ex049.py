#  Refaça o ex009, mostrando a tabuada de um número que o usuário
#  escolher, utilizando o LAÇO FOR.

n = int(input('Digite um número pra ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, n * c))