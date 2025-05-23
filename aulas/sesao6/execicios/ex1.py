#1 

# usuario = input('Me der um Nome de um time de Futebol ?')
# print(f'Time de futebol {usuario}')

#2 

#strip() usado para remover espaços

# time1 = input('Primeiro time:')
# if  time1.isnumeric():
#     print('erro')
# time2 = input('Segundo time:')
# if not time2.isnumeric():
#     print('erro')
# try:
#     time1_gol = int(input(f'Gols do time {time1}: '))
#     time2_gol = int(input(f'Gols do time {time2}: '))
# except:
#     print('erro digitou letras')

# print(
#     '-------------------- placar -------------------\n',
#         f'{time1} {time1_gol} X {time2_gol} {time2}\n'
#     '-------------------- placar -------------------\n',
# )

#3

# times = [
#     {'time':'vasco', 'pontos': 22},
#     {'time':'botafogo', 'pontos': 55},
#     {'time':'flamengo', 'pontos': 25}
# ]
# vencedor_pontos = 0
# vencedor_time = ''
# for i in times:
#     print(f' Time {i['time']} | Pontos: {i['pontos']}')
#     if i['pontos'] > vencedor_pontos:
#         vencedor_pontos = i['pontos']
#         vencedor_time = i['time']
# print(f'\n Time vencedor o maior pontuação {vencedor_time}: {vencedor_pontos}')

# 4

# def estatistica_jogos(vitoria, empate, derrota):
#     return (vitoria * 3 )+ (empate * 1) + (derrota * 0)

# vitoria = int(input('Vitorias: '))
# empate = int(input('Vitorias: '))
# derrota = int(input('Vitorias: '))

# resultado = estatistica_jogos(vitoria, empate, derrota)
# print(resultado)
    
# 5



