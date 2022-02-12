# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça pro usuário tentar descobrir qual foi esse número.
# Print na tela se o usuário venceu ou perdeu.

from random import randint # (randint) Faz um sorteio aleatório.
from time import sleep # (sleep) Faz uma pausa temporizada.

computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5 . Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS!! Você conseguiu me vencer!')
else:
    print('VOCÊ PERDEU!! Eu pensei no número {} e não no {}!'.format(computador, jogador))
