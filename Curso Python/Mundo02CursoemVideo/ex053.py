"""Crie um programa que leia uma frase qualquer e diga se ele é
um PALÍNDROMO, desconsiderando os espaços"""

frase = str(input('Digite uma frase: ')).strip().upper()
separar_as_palavras = frase.split()
juntar_as_palavras = ''.join(separar_as_palavras)
inverso = juntar_as_palavras[::-1]  # Fatiamento
'''inverso = ''
for letra in range(len(juntar_as_palavras)-1, -1, -1):
   inverso += juntar_as_palavras[letra]'''
print('O inverso da frase {} é {}'.format(juntar_as_palavras, inverso))
if inverso == juntar_as_palavras:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada NÃO É UM PALÍNDROMO!')
