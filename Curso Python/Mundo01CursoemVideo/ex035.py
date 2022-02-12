'''Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário
se elas podem ou não formar um triângulo.'''

print('-=-' * 10)
print('Analisando Triângulos')
print('-=-' * 10)

l1 = float(input('Insira a primeira medida: '))
l2 = float(input('Insira a segunda medida: '))
l3 = float(input('Insira a terceira medida: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 > l1 + l2:
    print('As respectivas medidas PODEM FORMAR um triângulo! ')
else:
    print('As respectivas medidas NÃO PODEM FORMAR um triângulo! ')
