"""Crie um programa que leia vários números inteiros pelo teclado
No final da execução, mostre a média entre todos os valores e qual foi o maior
e o menor valor lido. O programa deve perguntar ao usuário se ele quer
ou não continuar a digitar valores."""

resposta = 'S'
soma = quantidade = media = maior = menor = 0
while resposta in 'Ss':
    numero = int(input('Digite um número: '))
    soma += numero
    quantidade += 1
    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quantidade
print('Você digitou {} números e a média entre eles foi {}'.format(quantidade, media))
print('O maior valor digitado foi {} e o menor foi {}.'.format(maior, menor))
