# Crie um programa que leia um número Real qualquer pelo teclado e
# mostre na tela sua porção inteira.

from math import trunc
numero = float(input('Digite um número:'))
print('O número digitado foi {} e a sua porção Inteira é {}'.format(numero, trunc(numero)))

# Tbm é possível usar uma função interna do Python pra retornar o valor inteiro (int).
n = float(input('Digite um número'))
print('O número digitado foi {} e a sua porção Inteira é {}'.format(n, int(n)))
