"""
Filter
"""
# import statistics

# dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# media = statistics.mean(dados)

# print(media)

# #Esta lambda retorna todos os valores que são maiores que a media
# res = filter(lambda x: x > media, dados)
# print(list(res))

# #So existe uma vez na segunda excecução o valor some.
# print(f'Novamente: {list(res)}')

paises = ['', 'Argentina','', 'Brasil', '','Chile']

res = filter(None, paises)
#res2 = filter(lambda pais: len(pais) > 0, paises)
res3 = filter(lambda pais: pais != '', paises)

print(list(res))

print(list(res3))


