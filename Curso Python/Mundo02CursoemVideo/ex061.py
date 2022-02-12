"""Refaça o Ex051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos utilizando o while."""

print('Geradores de PA')
print('-=' * 10)

# utilizando FOR
primeiro = int(input('Primeiro termo: '))  # por onde começar a contagem.
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1 + 1) * razao
for c in range(primeiro, decimo, razao):
    print('{}'.format(c), end=' - ')
print('FIM')

#utilizando WHILE
p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
t = p
c = 1
while c <= 10:
    print('{} - '.format(t), end='')
    t += r
    c += 1
print('ACABOU')
