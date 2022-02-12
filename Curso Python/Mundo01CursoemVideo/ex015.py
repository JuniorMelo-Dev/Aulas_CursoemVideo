# Escreva um programa que pergunte a quantidade de Km percorridos por um carro
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos Km rodados? '))
dias = int(input('Quantos dias alugados? '))

dias_a_pagar = dias * 60
km_a_pagar = km * 0.15
total_a_pagar = dias_a_pagar + km_a_pagar
print('O valor de dias a pagar é de R${:.2f}'.format(dias_a_pagar))
print('O valor de km a pagar é de R${:.2f}'.format(km_a_pagar))
print('O valor total a pagar é de R${:.2f}'.format(total_a_pagar))
