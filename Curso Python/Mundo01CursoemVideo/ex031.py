# Faça um programa que pergunte a distância de uma viagem em Km. Depois calcule o preço da
# passagem, cobrando R$0,50 por Km para viagens de até 200Kmm e R$0,45 para viagens mais longas.

# Modo Condicional do tipo Composto...
distancia = float(input('Qual a distância da sua viagem? '))
print('Conforme informado acima, sua viagem tem {:.2f}Km'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('O preço da sua passagem será de R${:.2f}'.format(preço))


# Modo chamado IF simplificado...
distância = float(input('Qual a distância da sua viagem? '))
print('Conforme informado acima, sua viagem tem {:.2f}'.format(distância))
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('O preço da sua passagem será de R${:.2f}'.format(preço))
