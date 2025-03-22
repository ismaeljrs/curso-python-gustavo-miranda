import os

while True:
    print('=================  FAZER UMA LISTA DE COMPRAS =====================')
    print('\n')
    list_compras = []
    try:
        objetos = int(input('Quantos objetos deseja Adicionar nas listas: '))
    except:
        print('Você digitou letras em vez de números | Digite apenas números')
        print('>>> enter')
        input()
        os.system('clear')
        continue

    print('------- Objetos da Lista de Compras ---------')
    for i in range(objetos):
        usuario = str(input(f'{i+1} item da lista: '))
        list_compras.append(usuario)

    print('LISTA DE COMPRAS')
    print('-----------------')
    for i,l in enumerate(list_compras):
        print(f'{i}. {l}')
    print('-----------------')

    adiocionar_lista = str(input('Deseja adionar alguma coisa na lista? S - Sim | N - Não : '))
    if adiocionar_lista.lower() == 's':
        qnts_vezes = int(input('Quantas vezes deseja adicionar mais? '))
        for i in range(qnts_vezes):
            ad_lista = str(input('Adicionar: '))
            list_compras.append(ad_lista)

    elif adiocionar_lista.lower() == 'n':
        ...
    print('\n')
    deseja_excluir = str(input('Deseja exluir alguma coisa da sua lista?: S - Sim | N - Não :'))
    if deseja_excluir.lower() == 's':
        for i,l in enumerate(list_compras):
            print(f'{i}. {l}')
        desejo_exluir = int(input('Qual vc deseja excluir ____ Digite apenas numero: '))
        list_compras.pop(desejo_exluir)
    elif deseja_excluir.lower() == 'n':
        ... 
    print('\n')
    print('Ir ao Mercado: Lista de compras')
    print('==========================')
    for i,l in enumerate(list_compras):
        print(f'{i}. {l}')
    print('==========================')

    sair = input('Deseja criar uma outra lista?: S - Sim | N - Não : ')
    
    if sair.lower() == 's':
        os.system('clear')
    elif sair.lower() == 'n':
        break

    print('===============================================================================')

'''
    resolução do professor

"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('clear')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')

'''