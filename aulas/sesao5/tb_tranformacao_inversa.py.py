import numpy as np 
import os

while True:
    print('-------------------------------')
    print('Tranformação linear T: ℝⁿ → ℝⁿ')
    print('-------------------------------')
    input('Aperte enter // ')
    os.system('clear')

    print('\n')
    usu_colunas = input('Digite quantas colunas vai ter a matriz 2 ou 3: ')
    if not  usu_colunas.isnumeric():
        print('---------------------')
        print('Digite apenas números')
        print('---------------------')
        input('Aperte enter // ')
        os.system('clear')
        continue
    else:
        usu_colunas = int(usu_colunas)
    if usu_colunas not in [2,3]:
        print('----------------------------')
        print('Digite apenas 2 ou 3 colunas')
        print('----------------------------')
        input('Aperte enter // ')
        os.system('clear')
        continue
    else: 
        usu_linhas = input('Digite o número de linhas.....................: ')
        if not  usu_linhas.isnumeric():
            print('---------------------')
            print('Digite apenas números')
            print('---------------------')
            input('Aperte enter // ')
            os.system('clear')
            continue
        else:
            usu_linhas = int(usu_linhas)
        if usu_linhas != usu_colunas:
            print('-------------------------------------------------')
            print('Não e possivel formar uma Matriz quadrada (n x n)')
            print('-------------------------------------------------')
            input('Aperte enter // ')
            os.system('clear')
            continue
    print('\n')
    print(f'---- Inverção de matriz {usu_colunas}x{usu_linhas} ----')
    T = []
    try:
        for i in range(usu_linhas):
            linha = []
            for j in range(usu_linhas):
                valor = int(input(f'Digite o valor da posição [{i}] [{j}]: '))
                linha.append(valor)
            T.append(linha)
    except:
        print('---------------------')
        print('Digite apenas números')
        print('---------------------')
        input('Aperte enter // ')
        os.system('clear')
        continue
    print('---------')
    for linha in T:
        print(linha)
    print('---------')

    try: 
        A_inversa = np.linalg.inv(T)
        print("Matriz inversa T^-1:")
        print(A_inversa)
        break
    except:
        print('A Matriz T não e invertivel ')
        print('----------------------------')
        break
    