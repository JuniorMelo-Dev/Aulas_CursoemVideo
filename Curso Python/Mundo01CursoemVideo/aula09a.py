# Operação com Strings. Principais operações que vamos aprender são o: Fatiamento de String,
# Análise:
# len(Contar o tamanho da frase)....count(Contar determinada letra)....find(Retorna a posição da palavra e se não existir retorna -1).
# Transformação:
# replace(Trocar determinada palavra por outra)....upper(Jogar toda frase pra Maiúscula)....lower(Jogar toda frase pra Minúscula)....
# capitalize(Torna somente a primeira letra da frase em Maiúscula)....title(Transforma a primeira palavra em Maiúscula em toda a frase)....
# strip(Remove espaços antes e depois da frase)....rstrip(Remove espaços à direita da frase)....lstrip(Remove os espaços à esquerda da frase).
# Divisão:
# split(Divide a frase em blocos conforme os espaços entre as palavras)
# Junção:
# join(Faz a junção entre as palavras com caracteres que se deseja).

frase = '  Aprendendo Python com Profº Guanabara  !!  '
print(len(frase))
print(frase.count('e'))
print(frase.find('Python'))
print(frase.find('Casa'))
print(frase.replace('Aprendendo','Ensinando'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())
print(frase.split(), '-'.join(frase))
