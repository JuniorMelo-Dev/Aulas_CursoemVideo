# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
# e condição de pagamento:
""" à vista dinheiro/cheque: 10% desconto
    à vista no cartão: 5% desconto
    em até 2x no cartão: sem juros
    3x ou mais no cartão: 20% juros..."""

print('{:=^40}'.format(' \033[1;31mLOJAS JLBH E CIA\033[m '))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque \033[1;32m10% desconto\033[m
[ 2 ] à vista cartão \033[1;32m05% desconto\033[m
[ 3 ] 2x no cartão \033[4;33msem juros\033[m
[ 4 ] 3x ou mais no cartão \033[1;4;31m20% de juros\033[m''')
opção = int(input('Qual é a forma de pagamento? '))
if opção == 1:
    total = preço - (preço * 0.10)
elif opção == 2:
    total = preço - (preço * 0.05)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opção == 4:
    total = preço + (preço * 0.20)
    parcelas = int(input('Quantas parcelas? '))
    parcela = total / parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcelas, parcela))
else:
    total = preço
    print('\033[1;31mOPÇÃO DE PAGAMENTO INVÁLIDA\033[m. Tente novamente!')
print('Sua compra de \033[1;4mR${:.2f}\033[m vai custar \033[1;4mR${:.2f}\033[m no final.'.format(preço, total))
