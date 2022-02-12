"""Melhore o EX061, perguntando p/ o usuário se ele quer mostrar
mais alguns termos. O programa encerrará quando ele disser que quer
mostrar 0 termos."""

print('Geradores de PA')
print('-=' * 10)

p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
t = p
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print('{} - '.format(t), end='')
        t += r
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos vc quer mostrar a mais? '))
    print('------Fim do Programa...------')
print('PA finalizada com \033[1;4;31m{} termos\033[m mostrados.'.format(total))
