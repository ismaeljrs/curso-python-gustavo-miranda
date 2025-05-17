

import copy


try:
    nome_criadores = int(input('  Quantos criadores tem?: '))
    nomes = []

    # colocar dentro de uma lista nome dos criadores 
    for i in range(nome_criadores):
        nome = input(f'{i} Nome: ')
        if not nome.isnumeric():
               
        nomes.append(nome)
    print(nomes)
    nomes2 = copy.deepcopy(nomes)
    print(f'nomes lista 2 = {nomes2}')
except ValueError:
            print('Digite apenas números')



# def fora(x):
#     a = x

#     def dentro():
#         return a
#     return dentro

# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1())
# print(dentro2())