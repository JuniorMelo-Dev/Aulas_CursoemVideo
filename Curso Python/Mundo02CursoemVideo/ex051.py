# Desenvolva um programa que leia o primeiro termo e a razão
# de uma PROGRESSÃO ARITMÉTICA. No final, mostre os 10 primeiros
# termos dessa PA.

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1 + 1) * razao
for c in range(primeiro, decimo, razao):
    print('{}'.format(c), end=' - ')
print('FIM')
