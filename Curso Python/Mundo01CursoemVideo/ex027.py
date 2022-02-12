# Faça um programa que leia o nome completo de uma pessoa, mostrando
# em seguida o primeiro e o último nome separadamente.

nome = str(input('Qual é o seu nome completo? ')).strip()
n = nome.split()

print('O seu 1º nome é: {}'.format(n[0]))
print('O seu último nome é: {}'.format(n[len(n)-1]))
