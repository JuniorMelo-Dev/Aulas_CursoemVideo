"""Melhore o desafio abaixo (ex028), só que agora o jogador vai tentar
adivinhar até acertar e mostrar quantos palpites foram necessários pra vencer"""

from random import randint # (randint) Faz um sorteio aleatório.
from time import sleep # (sleep) Faz uma pausa temporizada.

'''pc = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5 . Tente adivinhar...')
print('-=-' * 20)
j = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(1.2)
if j == pc:
    print('PARABÉNS!! Você conseguiu me vencer!')
else:
    print('VOCÊ PERDEU!! Eu pensei no número {} e não no {}!'.format(pc, j))'''

notebook = randint(0, 10)
print('Sou seu notebook... Acabei de pensar em um número entre 0 e 10.')
print('Será que vc consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpites += 1
    if jogador == notebook:
        acertou = True
    else:
        if jogador < notebook:
            print('Mais... Tente mais uma vez.')
        elif jogador > notebook:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
