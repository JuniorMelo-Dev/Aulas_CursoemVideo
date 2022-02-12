# Crie um programa que leia o ano de nascimento de um atleta e mostre a sua categoria,
# de acordo com a sua idade:

""" Até 09 anos: MIRIM
    Até 14 anos: INFANTIL
    Até 19 anos: JÚNIOR
    Até 25 anos: SÊNIOR
    Acima de 25 anos: MASTER"""

from datetime import  date
ano_atual = date.today().year      #importação da função data atual.

nasc = int(input('Ano de nascimento: '))
idade = ano_atual - nasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
