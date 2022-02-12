# 'Um professor quer sortear um doas seus quatro alunos p/ apagar o
# quadro. Faça um programa que ajude ele, lendo o nome dos alunos e
# escreva na tela o nome do aluno sorteado.

import random
a1 = str(input('Primeiro aluno:'))
a2 = str(input('Segundo aluno:'))
a3 = str(input('Terceiro aluno:'))
a4 = str(input('Quarto aluno:'))
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print('O aluno sorteado foi: {}'.format(escolhido))
