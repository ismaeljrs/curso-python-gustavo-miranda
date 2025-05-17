'''
* Calculadora While *

'''
import os
cont = 0
while True:
    cont += 1
    os.system('clear')
    print('ESCOLHA QUAIS OPERAÇÃO DESEJA ESCOLHER:')
    print('1 - + MAIS ')
    print('2 - - MENOS ')
    print('3 - X VEZES ')
    print('4 - / DIVISÃO ')
    try:
        escolha = int(input('Escolha: '))
        if escolha <= 4:
            num_1 = float(input('Digite o 1o. Número: '))
            num_2 = float(input('Digite o 2o. Número: '))
        else:
            print('Digite apenas de ate 4 ')
            enter = input('Aperte enter para continuar')
            continue 

    except:
        print('Digite apenas números')
        print('--'*5)
        enter = input('Aperte enter para continuar')
        continue
    resul = 0
    if escolha == 1:
        resul = num_1 + num_2
        print(resul)

    if escolha == 2:
        resul = num_1 - num_2
        print(resul)
    elif escolha == 3:
        resul = num_1 * num_2
        print(resul)
    elif escolha == 4:
        resul = num_1 / num_2
        print(resul)

    sair = input('Deseja continuar S ou N?').lower()
    if sair == 's':
        continue
    if sair == 'n':
        print(5*'--','FIM','--'*5)
        break
print(f'Total de Tentativas foi {cont}')




    

    