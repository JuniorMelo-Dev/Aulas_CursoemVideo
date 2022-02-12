# Crie um programa e faça-o jogar Jokenpô com você.

from random import randint
from time import sleep

itens = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0, 2)
print('''\033[1;4;7;30;47mOPÇÕES\033[m
[ 0 ] \033[1;31mPEDRA\033[m
[ 1 ] \033[1;31mPAPEL\033[m
[ 2 ] \033[1;31mTESOURA\033[m''')
jogador = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
print('-=-' * 11)
print('PC jogou {}'.format(itens[pc]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=-' * 11)
if pc == 0:   # o pc jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU !!')
    elif jogador == 2:
        print('PC VENCEU !!')
elif pc == 1:   # o pc jogou PAPEL
    if jogador == 0:
        print('PC VENCEU !!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU !!')
elif pc == 2:   # o pc jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCEU !!')
    elif jogador == 1:
        print('PC VENCEU !!')
    elif jogador == 2:
        print('EMPATE')
else:
    print('JOGADA INVÁLIDA!')