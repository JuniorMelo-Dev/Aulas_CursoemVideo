# Ordem de Precedência para Operadores Aritméticos
# 1º -> '()' parentêses
# 2º -> '**' potência
# 3º -> '*' multiplicação; '/' divisão; '//' divisão inteira; '%' resto da divisão
# 4º -> '+ e -' adição e subtração
# Raíz quadrada 'n**(1/2)' e Raíz cúbica 'n**(1/3)


n1 = int(input('Um valor:'))
n2 = int(input('Outro valor:'))
so = n1 + n2
su = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
rd = n1 % n2
rq = n1 **(1/2)
rc = n1 **(1/3)
print('A soma é {}, a subtração é {}, o produto é {} e a divisão é {:.3f}'.format(so, su, m, d))
print('divisão inteira {}, potência {}, o resto da divisão {}, a raíz quadrada é {:.3f} e a raiz cúbica é {:.3f}'.format(di, e, rd, rq, rc))



