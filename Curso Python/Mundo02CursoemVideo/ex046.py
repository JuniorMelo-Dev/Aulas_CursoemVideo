# Faça um programa que mostre na tela uma contagem regressiva para
# o estouro de fogos de artifícios, indo de 10 até 0, com uma pausa de
# 1 segundo entre a contagem.

from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('Boom...Boom..Pá pá pá...')
