# Escreva um programa que leia um valor em metros e o exiba
# convertido em centímetros e milímetros.

medida = float(input('Digite um valor:'))
cm = medida * 100
mm = medida * 1000
print('Analisando o valor {} '
      '\nem \033[1;4;31mcentímetros\033[m temos {:.0f}cm '
      '\ne em \033[1;4;36mmilímetros\033[m temos {:.0f}mm'.format(medida, cm, mm))
