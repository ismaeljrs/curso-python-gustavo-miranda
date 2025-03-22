"""
autor : Ismael Jorge Brandão
Profesor : Gustavo Miranda
"""
import os
import random

comput = 0
usuario = 0
flag = True
while flag:
    def titulo():
        print('========================================')
        print('Bem vindo ao jogo pedra Papel e Tesoura')
        print('========================================')

    def placar(a=0 ,b=0):
        print(f'Você: {a}')
        print(f'Computador: {b}')
        print(
            f'Escolha seu lance\n'
            f'0 - Papel | 1 - Pedra | 2 - Tesoura\n'
        )

    def lance(eu,compt):
        global usuario, comput
        if eu == compt :
            return 'Empate'
        elif (eu == 'pedra' and compt == 'tesoura' ):
            usuario += 1
            return 'Vencedor: Usuário'
        elif (eu == 'tesoura' and compt == 'papel'):
            usuario += 1
            return 'Vencedor: Usuário'
        elif(eu == 'papel' and compt == 'pedra'):
            usuario += 1
            return 'Vencedor: Usuário'
        else:
            comput += 1
            return 'Vencedor: Computador'
            
        
    def jogada(eu,compt):
        print('Jogadas:')
        print(f'*{'=='*15}*')
        print(f' Sua jogada foi......: {eu}')
        print(f' Jogada do computador: {compt}')
        
        resultado = lance(eu,compt)
        if resultado == 'Empate':
            print('Empate!')
        elif resultado == 'Vencedor: Usuário':
            print('Parabéns, você venceu!')
        else:
            print('Computador venceu')     
            
        print(f'*{'=='*15}*\n')

    lista = [
        ['papel'],
        ['pedra'],
        ['tesoura']
    ]

    titulo()
    print('\n')
    placar(usuario,comput)

    computador = random.choice(lista)[0]

    try:
        escolha = int(input('Escolha: '))
        if escolha > 2:
            raise IndexError('Digite apenas de 0 ate 2')  
        if escolha == ' ':
            raise ValueError('Erro: Digite um valor válido ok?')
    except IndexError as e:
        print(e)
        print('>>>> Pressione Enter para tentar novamente.')
        input()
        continue
    except ValueError:
        print('Erro: Digite um valor válido ok?')
        print('>>>> Pressione Enter para tentar novamente.')
        input()
        continue

    escolha = lista[escolha][0]
    lance(escolha, computador)
    jogada(escolha, computador)

    flag1 = True
    while flag1:
        sair = str(input('Deseja jogar novamente: S - continuar | N - Sair: '))

        if sair.lower() == 's':
            flag1 = False
            os.system('clear')
        elif sair.lower() == 'n':
            flag1 = False
            flag = False