# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

# Método de fazer o código exigido sem precisar importar nenhuma lista.
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa desse triângulo será {:.2f}'.format(hi))

# Método com inclusão da importação do Hypot (Hipotenusa).
from math import hypot
cateto_oposto = float(input('Comprimento do cateto oposto:'))
cateto_adjacente = float(input('Comprimento do cateto adjacente:'))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print('A hipotenusa desse triângulo será {:.2f}'.format(hipotenusa))
