"""Crie um programa que leia o ano de nascimento de 7 pessoas.
No final mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores."""

from datetime import date
ano_atual = date.today().year # verificação do ano atual com o import datetime.
total_maior = 0
total_menor = 0
for n_pessoas in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(n_pessoas)))
    idade = ano_atual - nasc
    if idade >= 18:
        total_maior += 1
    else:
        total_menor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(total_maior))
print('E tbm tivemos {} pessoas menores de idade'.format(total_menor))
