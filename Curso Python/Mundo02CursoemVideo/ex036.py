# Escreva um programa para avaliar um empréstimo bancário pra
# compra de uma casa. O programa vai perguntar o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar.

# Calcule o valor da prestação mensal, sabendo que ele não
# pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('Qual o valor do imóvel: R$ '))
salario_comprador = float(input('Qual o salário mensal do comprador: R$ '))
financiar_em = int(input('Em quanto tempo será o financiamento: '))
mensalidade = valor_casa / (financiar_em * 12)
minimo = float(salario_comprador * 0.30)
print('Para financiar o imóvel de \033[4;33mR${:.2f}\033[m em {} anos'.format(valor_casa, financiar_em))
print('a mensalidade será de \033[1;32mR${:.2f}\033[m'.format(mensalidade))
if mensalidade <= minimo:
    print('Parabéns empréstimo \033[1;4;32mCONCEDIDO!!\033[m')
else:
    print('Empréstimo \033[1;4;31mNEGADO!\033[m Verifique as condições do financiamento!!')
