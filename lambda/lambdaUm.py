#def funcao(x):
#    """[summary]
#    Lambda é uma função sem nome
#    Func em Python:

#   def soma(a,b):
#        retun a + b
#    """
#    return 3 * x + 1
#print(funcao(7))


# Exemplo de Lambida

#calc = lambda x: 3 * x +1
#print(calc(7))


## Expressao lambda com multiplas entradas

# nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

# print(nome_completo(' angelina', 'JOLIE'))

# amar = lambda: 'Como nao amar python'

# uma = lambda x: 3 * x + 1

# duas = lambda x,y: (x * y) ** 0.5

# tres = lambda x,y,z: 3 / ( 1/ x + 1 / y + 1 / z )

# print(amar())
# print(uma(6))
# print(duas(5,7))
# print(tres(3,6,9))

# Se passarmos mais argumentos do que parametros vamos ter um TypeError

# autores = ['Issac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert', 'H. G. Wells']

# print(autores)

# autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

# print(autores)

#Função quadratica
#f(x) = a * x ** 2 + b * x + c

# def geradora_funcao_quadratica(a,b,c):
#     """[summary]
#         Retorna f(x) = a * x ** 2 + b * x + c

#     Args:
#         a ([type]): [description]
#         b ([type]): [description]
#         c ([type]): [description]
#     """
#     return lambda x: a * x ** 2 + b * x + c
# teste = geradora_funcao_quadratica(2,3,-5)

# print(teste(0))
# print(teste(1))
# print(teste(2))
