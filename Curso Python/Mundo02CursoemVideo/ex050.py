#  Desenvolva um programa que leia 6 números inteiros e mostre
#  a soma apenas daqueles que forem pares, sendo ímpar desconsiderar.

acumulador = 0
contador = 0
for c in range(1, 7):
    num = int(input('Digite {}º número: '.format(c)))
    if num % 2 == 0:
        contador += 1
        acumulador += num
print('Você informou {} número(s) PAR(es) e a soma foi {}'.format(contador, acumulador))
