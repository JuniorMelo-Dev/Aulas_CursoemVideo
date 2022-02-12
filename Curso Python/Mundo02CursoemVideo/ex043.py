# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu (IMC) Índice de Massa Corporal e mostre seu status de acordo
# com a tabela abaixo:

""" abaixo de 18,5: Abaixo do peso
    entre 18,5 e 25: Peso ideal
    25 até 30: Sobrepeso
    30 até 40: Obesidade
    Acima de 40: Obesidade Mórbida..."""

peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (mt) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está \033[4;7;36mABAIXO DO PESO\033[m normal.')
elif 18.5 <= imc < 25:
    print('Você está na faixa de \033[1;4;32mPESO IDEAL\033[m.')
elif 25 <=  imc < 30:
    print('Você está na faixa de \033[4;33mSOBREPESO\033[m.')
elif 30 <= imc < 40:
    print('Você está na faixa de \033[4;36mOBESIDADE\033[m.')
elif imc >= 40:
    print('Você está na faixa de \033[4;31mOBESIDADE MÓRBIDA\033[m, \033[4;31mCUIDADO\033[m...')