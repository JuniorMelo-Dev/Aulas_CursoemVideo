"""Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores
M ou F. Caso esteja errado, peça pra digitar novamente até obter valor válido"""

s = str(input('Informe o sexo da pessoa: [M/F] ')).strip().upper()[0]  # Tratamento de string. FATIAMENTO
while s not in 'MF':
    s = str(input('Dados inválidos. Favor insira o sexo válido: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(s))
