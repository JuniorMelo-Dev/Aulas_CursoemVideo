# Faça um programa que leia 3 números e mostre qual é o MAIOR e qual o MENOR.

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# Verificando o menor valor...
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando o maior valor...
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O MENOR valor digitado foi {}.'.format(menor))
print('O MAIOR valor digitado foi {}.'.format(maior))
