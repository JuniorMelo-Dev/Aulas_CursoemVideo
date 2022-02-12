# Faça um algoritmo que leia o salário do funcionário
# e mostre seu novo salário, com 15% de aumento.

s = float(input('Insira o salário do funcionário R$'))
a = s * 0.15
ns = s + (s * 0.15)

print('Com base no salário anterior de R${:.2f}'.format(s))
print('O funcionário recerá um aumento de R${:.2f}'.format(a))
print('O funcionário com o aumento de 15% irá receber R${:.2f}'.format(ns))
