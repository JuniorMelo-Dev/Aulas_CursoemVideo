# Faça um algoritmo que leia o preço de um produto e mostre seu
# novo preço, com 5% de desconto.

preço = float(input('Digite o preço do item R$'))
desconto = preço * 0.05
novo_preço = preço - desconto
print('O desconto do produto é {:.2f}'.format(desconto))
print('O novo preço com desconto é {:.2f}'.format(novo_preço))
