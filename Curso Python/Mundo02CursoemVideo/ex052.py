"""Faça um programa que leia um número inteiro e diga se ele
é ou não um número primo"""

num = int(input('Digite um número: '))# Números PRIMOS somente são divisíveis por 1 e # por ele mesmo.
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        total += 1
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes.'.format(num, total))
if total == 2: # Tem de ser divisível somente 2 vezes pra ser PRIMO.
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
