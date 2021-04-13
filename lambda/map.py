"""
Map

Com Map fazemos mapeamento de valores para função.

import math

def area(r):
    #[Calcula a area de um circulo com o raio 'r']
    Args:
        r ([type]): [description]
    return math.pi * (r ** 2)

print(area(2))
print(area(5.3))

raios = [2,5,7.1,0.3]

#Forma Comum
areas = []
for r in raios:
    areas.append((area(r)))

print(areas)

# Forma 2 com Map

areas = map(area, raios)
print(areas)
print(type(areas))
print(list(areas))

# Forma 3 Map com Lambda

print("Forma com lambda")
print(list(map(lambda r: math.pi * (r ** 2),raios)))

#OBS: Apos utilizar a func map ele zera os resultados
"""


cidades = [('Berlin',29),('Cairo',36),('Nova York',28),('Londres',22)]

print(cidades)

# f = 9/5 * c + 32

#Lambda

c_para_f = lambda dado: (dado[0], (9/2) * dado[1] + 32)
print(list(map(c_para_f,cidades)))