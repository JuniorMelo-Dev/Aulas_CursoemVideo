# Carregando bibliotecas com o 'import e from/import'
# no Pythone usando recursos adicionais nos programas
# utilizando módulos built-in e módulos externos oferecidos no Pypi.

# from math import sqrt Esse import nos tráz somente uma função específica no caso sqrt.
import math  # Esse import nos tráz todas as funções de Math.
num = int(input('Digite um número:'))
raiz = math.sqrt(num)
print('A raíz de {} é igual a {:.2f}'.format(num, raiz))
