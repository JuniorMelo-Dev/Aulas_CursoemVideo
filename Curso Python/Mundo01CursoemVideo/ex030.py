# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input('ÍMPAR ou PAR? Digita ai um número: '))
resultado = numero % 2 #(Se o resto da divisão for 0 o número é PAR, se for 1 o número é ÍMPAR)
if resultado == 0:
    print('O número {} é PAR'.format(numero))
else:
    print('O número {} é ÍMPAR'.format(numero))
