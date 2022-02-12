'''Criando estrutras condicionais aninhadas,
usando if,,elif,,else...'''

nome = str(input('Qual é o seu nome? '))
if nome == 'Junior':
    print('Que nome lindo!')
elif nome == 'Pedro' or nome == 'Marcia' or nome == 'Paulo':
    print('Belo nome heim...!')
elif nome in 'Ana lucia Jonas Bento':
    print('Seu nome é Pequeno..')
else:
    print('Que nome simples...!')
print('Não tenha um bom dia {}, tenha um ótimo dia!'.format(nome))
