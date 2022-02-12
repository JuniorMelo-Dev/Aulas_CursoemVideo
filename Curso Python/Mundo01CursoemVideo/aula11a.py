"""Aula de Inserir cores no Terminal Padrão ANSI..."""

# reprensentar cores com o código " \033 [ STYLE 0 ; TEXTO 33 ; BACKGROUND 44 m

# Códigos pra STYLE (Estilo da letra) -> 0 NONE sem estilo; 1 BOLD negrito;
# 4 UNDERLINE sublinhado e 7 NEGATIVE inverte as configurações...

# Códigos pra TEXTO (Cores das letras) -> de 30 ao 37 (30 Preto, 31 Vermelho, 32 Verde,
# 33 Amarelo, 34 Azul, 35 Magenta, 36 Ciano e 37 Cinza) respectivamente...

# Códigos pra BACKGROUND (Cores de Fundo ao Texto) -> de 40 ao 47 (Mesmas cores do código
# TEXTO)...

print('\033[30;47mEai Abençoado!!\033[m')

a = 45
b = 33
print('Os valores são \033[31m{}\033[m e \033[33m{}\033[m'.format(a, b))

nome = 'Junior Melo'
print('Eai blz, {}{}{}!'.format('\033[1;4;32m', nome, '\033[m'))

nome = 'Junior'
cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'magenta':'\033[35m',
         'pretoebranco':'\033[7;30m'}
print('Eai abençoado, {}{}{}!!'.format(cores['verde'], nome,
                                       cores['limpa']))
