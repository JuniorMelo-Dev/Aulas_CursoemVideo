# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date
ano = int(input('Que ano você quer analisar? Insira 0 para retornar o ano atual: '))
if ano == 0:
    ano = date.today().year
    print('O ano atual é {}.'.format(ano))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('E o ano {} é BISSEXTO.'.format(ano))
else:
    print('E o ano {} NÃO é BISSEXTO.'.format(ano))
