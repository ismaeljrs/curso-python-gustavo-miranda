#execicio que duplica , triplica , quadruplica

def duplica(*numero):
    total = 1
    for i in numero:
        total *= i 
    return total * 2  
def Triplica(*numero):
    total = 1
    for i in numero:
        total *= i
    return total * 3

def Quadriplicar(*numero):
    total = 1
    for i in numero:
        total *= i
    return total * 4
def executar(funcao,*args):
    return funcao(*args)   
 
soma = executar(duplica,1,2,3,4)
triplicar = executar(Triplica,1,2,3,4)
quadriplicar = executar(Quadriplicar,1,2,3,4)

print(f'numero duplicado {soma}')
print(f'numero triplicado {triplicar}')
print(f'numero triplicado {quadriplicar}')

