# criar uma finção que duplica , triplica , multiplica 

# def duplicar(numero):
#     return  numero * 2
# def triplicar(numero2):
#     return  numero2 * 3

# def quadruplicar(numero3):
#     return  numero3 * 4

# print(duplicar(2))
# print(triplicar(3))
# print(quadruplicar(4))


'''
USANDO CLOSURE
'''

def cria_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

    

duplicar = cria_multiplicador(2)
triplicar = cria_multiplicador(3)
quadruplicar = cria_multiplicador(4)

print(duplicar(2))
print(triplicar(3))
print(quadruplicar(4))



