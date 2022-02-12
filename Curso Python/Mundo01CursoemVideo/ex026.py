# Crie um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição ela aparece a 1ª vez.
# Em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).upper().strip()

print('A letra A aparece {} vezes na frase acima'.format(frase.count('A')))
print('A letra A aparece a 1ª vez na posição: {}'.format(frase.find('A')+1))
print('A letra A aparece por último na posição {}:'.format(frase.rfind('A')+1))
