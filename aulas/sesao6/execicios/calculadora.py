'''
autor: Ismael jorge 
Objetivo: Calculadora

'''


def calcular(op , escol1, escol2):
    if op == 1:
        return escol1 + escol2
    elif op == 2:
        return escol1 - escol2
    elif op == 3:
        return escol1 / escol2
    elif op == 4:
        return escol1 % escol2
    elif op == 5:
        return escol1 * escol2
    else:
        return 'Erro'

def historico_txt(op, usu_escolha1,usu_escolha2, resultado):
    with open('historico.txt', 'a', encoding='utf-8') as arquivo:
        print('-------------------- Historico ---------------------', file=arquivo)
        if op == 1:
            print(f'{usu_escolha1} + {usu_escolha2} = {resultado}', file=arquivo)
        elif op == 2:
            print(f'{usu_escolha1} - {usu_escolha2} = {resultado}', file=arquivo)
        elif op == 3:
             print(f'{usu_escolha1} / {usu_escolha2} = {resultado}', file=arquivo)
        elif op == 4:
            print(f'{usu_escolha1} % {usu_escolha2} = {resultado}', file=arquivo)
        elif op == 5:
            print(f'{usu_escolha1} % {usu_escolha2} = {resultado}', file= arquivo)
        print('----------------------------------------------------', file=arquivo)


tot = 0
operadores = {
    1 : 'Mais',
    2 :'Menos',
    3 :'Divisão',
    4 :'Por cento',
    5 :' vezes '
}
while True:

    print('Operadores')
    for i, oper in operadores.items():
        print(f'{i} :  {oper}')

    op = int(input('Digite qual operavcao que vai querer: '))

    usu_escolha1 = int(input('Digite o 1o. Número: '))
    usu_escolha2 = int(input('Digite o 2o. Número: '))

    resultado = calcular(op, usu_escolha1, usu_escolha2)
    print(resultado)
    tot += 1
    historico_txt(op, usu_escolha1,usu_escolha2, resultado)
    opcao_sair = input('Deseja continuar ? s/n').lower()
    if opcao_sair == 's':
        break


    




