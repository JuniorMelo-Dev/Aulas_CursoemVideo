# 'O mesmo professro da aula 19 quer mais uma vez sortear a ordem
# de apresentação de trabalhos dos alunos. Faça um programa que leia o nome
# dos quatro alunos e mostre a ordem sorteada.

import random
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)
