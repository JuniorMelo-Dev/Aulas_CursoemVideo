# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
# de tinta necessária pra pintá-la. Sabendo que cada litro de tinta, pinta uma área de 2m².

larg = float(input('Insira a medida largura da parede:'))
alt = float(input('Insira a medida altura da parede:'))
área = larg * alt
print('A parede mencionada tem {}x{} e sua área é de {:.2f}m².'.format(larg, alt, área))
tinta = área / 2
print('Para pintar a parede mencionada será necessário de {:.2f}lts de tinta.'.format(tinta))
