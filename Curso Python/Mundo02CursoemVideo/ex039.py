# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é hora exata de se alistar ou se já passou do tempo do alistamento.
# Mostre tbm o tempo que falta ou o prazo que passou.

from datetime import date

ano_atual = date.today().year


nasc = int(input('Ano de nascimento:'))
idade = ano_atual - nasc
print('Quem nasceu em {} tem \033[4;33m{}\033[m anos em {}.'.format(nasc, idade, ano_atual))
if idade == 18:
    print('Você tem que se alistar \033[4;31mIMEDIATAMENTE!\033[m')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam \033[4;32m{}\033[m anos para o seu alistamento.'.format(saldo))
    ano = ano_atual + saldo
    print('Seu alistamento será em \033[4;33m{}\033[m.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há \033[4;31m{} anos\033[m.'.format(saldo))
    ano = ano_atual - saldo
    print('Seu alistamento foi em \033[1;4;30;43m{}\033[m.'.format(ano))
