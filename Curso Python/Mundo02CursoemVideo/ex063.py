"""Escreva um programa que leia um número N inteiro e mostre
na tela os N primeiros elementos de uma sequência de Fibonacci."""

print('-' * 30)
print('----\033[1:4:33mSequência de Fibonacci\033[m----')
print('-' * 30)

n = int(input('"quantos termos vc quer mostrar? '))
t1 = 0
t2 = 1
print('~' * 30)
print('{} - {}'.format(t1, t2), end='')
c = 3
while c <= n:
    t3 = t1 + t2
    print(' - {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1
print(' - FIM')
print('~' * 30)