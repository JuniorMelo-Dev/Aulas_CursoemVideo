# Faça um programa que leia um número na tela o seu sucessor e seu antecessor

n = int(input('Digite um número:'))
a = n - 1
s = n + 1
print('Analisando o valor {}\nseu \033[1;4;32mAntecessor\033[m é {} '
      '\ne o \033[1;4;33mSucessor\033[m é {}'.format(n, a, s))

