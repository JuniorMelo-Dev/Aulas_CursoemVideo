# Escreva um programa que leia um número inteiro qualquer
# e peça ao usuário escolher qual será a base de conversão:
# --1 p/ binário; --2 p/ octal; --3 p/ hexadecimal...

numero = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(numero, bin(numero))) # Números 0 e 1
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero, oct(numero))) # Números de 0 a 7
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero, hex(numero))) # Números de 0 a 9 e de A a F
else:
    print('Opção inválida. Tente novamente..')
