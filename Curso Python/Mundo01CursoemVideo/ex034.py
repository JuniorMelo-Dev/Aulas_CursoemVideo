# Escreva um programa que pergunte o salário de um funcionário e calcule o valor de
# um determinado aumento. Para salários superiores a R$1250,00 calcule um aumento de 10%.
# Para os salários inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual o salário atual do funcionário? R$ '))
if salario <= 1250:
    aumento = salario + (salario * 0.15)
else:
    aumento = salario + (salario * 0.10)
print('O funcionário que ganhava {:.2f} vai passar a ganhar {:.2f}'.format(salario, aumento))
