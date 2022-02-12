# Faça um programa que calcule a soma entre todos os números ímpares
# que são múltiplos (divisores) de 3 e que se encontram no intervalo de 1 até 500.

a = 0  # a de ACUMULADOR
c = 0  # c de CONTADOR
for soma in range(1, 501, 2):
    if soma % 3 == 0:
        print(soma)
        c += 1
        a += soma
print('O somatório dos {} valores acima DIVISORES de 3 é: {}'.format(c, a))
