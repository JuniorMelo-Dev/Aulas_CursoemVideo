# Crie um algoritmo que leia um número e mostre o seu dobro,
# triplo e raíz quadrada

n = int(input('Digite um número:'))
d = n * 2
t = n * 3
rq = n ** (1/2)
print('O \033[1;4;33mdobro\033[m de {} é \033[1;4;33m{}\033[m '
      '\no \033[1;4;31mtriplo\033[m de {} é \033[1;4;31m{}\033[m '
      '\na \033[1;4;34mraíz quadrada\033[m de {} é \033[1;4;34m{:.1f}\033[m '.format(n, d, n, t, n, rq))

