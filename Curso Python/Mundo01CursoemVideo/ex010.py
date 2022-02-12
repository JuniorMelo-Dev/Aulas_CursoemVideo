# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos Dólares ela pode comprar. Data do exercício 18/09/2021

na_carteira_tem = float(input('Na sua carteira tem R$:'))
dolar = na_carteira_tem / 5.29
euro = na_carteira_tem / 6.20
iene_japones = na_carteira_tem / 0.048
print('Com R${:.2f} você pode comprar \033[4;36m{:.2f}\033[m dólares americanos'.format(na_carteira_tem, dolar))
print('Com R${:.2f} você pode comprar \033[4;33m{:.2f}\033[m euros'.format(na_carteira_tem, euro))
print('Com R${:.2f} você pode comprar \033[4;31m{:.2f}\033[m ienes japones'.format(na_carteira_tem, iene_japones))
