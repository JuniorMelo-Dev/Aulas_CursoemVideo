# Escreva um programaque leia a velocidade de um carro. Se ele ultrapassar 80Km/h, 
# moostre uma mensagem que ele foi multado. A multa vai custar R$7,00 por cada
# Km acima do limite.

velocidade = float(input('Qual a velocidade atual do veículo? '))
if velocidade > 80:
    print('VOCÊ FOI MULTADO! Pois você excedeu o limite permitido de 80Km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa por excedente no valor de R${:.2f}!'.format(multa))
else:
    print('Tenha um Bom dia!  Dirija com segurança!')
