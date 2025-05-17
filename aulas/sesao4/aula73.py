#nao e muito comum print dentro de funçoes usa mais return 

'''
crie mais 2 funções no estilo mensagem_do_tecnico, com diferentes tipos de comandos.
Depois use a função executa_comando() para executá-las com jogadores diferentes. Exemplo:
'''
# def mensagem_tecnico(comando, jogador):
#     return f'{comando},ola aqui  {jogador}'

# def executar_comando(funcao, *args):
#     return funcao(*args)

# print(executar_comando(mensagem_tecnico,'Corre para o ataque', 'neymar'))
#execicio 1 
# def mensagem_tecnico(emogi,jogador):
#     return f'{emogi}. Vamos {jogador}! voce joga muito'

# def executar_comando(funcao,*args):
#     return funcao(*args)

# print(executar_comando(mensagem_tecnico, ' :) ','neymar'))
#execicio 2 
'''
---------terminal---------
⚽ Vinícius Jr, aqueça-se!
🔥 Gabigol, confio em você! Vamos vencer!
🔁 Sai Fred, entra Ronaldo!
'''
# def chamar_aquecimento(emogi,jogador):
#     return f'{emogi} {jogador} aqueça-se!'

# def motivacao_especial(emogi,jogador):
#     return f'{emogi} {jogador}, confio em você! Vamos vencer!'

# def fazer_uma_substituicao(emogi,jogador):
#     return f'{emogi} Sai {jogador}, entra Ronaldo!'

# def executar(funcao,*args):
#     return funcao(*args)
    
# print(executar(chamar_aquecimento, '⚽', 'Vinícius Jr'))
# print(executar(motivacao_especial ,'🔥', 'Gabigol'))
# print(executar(fazer_uma_substituicao,'🔁', 'Fred'))
#execicio 3 

'''
terminal
🔥 Gabigol, confio em você!
⚽ Vinícius Jr, aqueça-se, pode entrar a qualquer momento!
💊 Neymar, vamos cuidar bem da sua recuperação!
🎉 Bem-vindo ao time, Ronaldo! Mostre seu talento!

'''

def  painel_tatico(funcao,*jogador,**status):
    # for i in jogador:
    #     print(i)
    # for i in status:
    #     print(i)
    return funcao(*jogador,**status)


def motivar_jogador(emogi,nome):
    return f'{emogi} {nome}, confio em você!'
def preparar_para_reserva(emogi,nome):
    return f'{emogi} {nome}, aqueça-se, pode entrar a qualquer momento!'
def cuidar_lesionado(emogi,nome):
    return f'{emogi} {nome}, vamos cuidar bem da sua recuperação!'
def estreia_jogador(emogi,nome):
    return f'{emogi} Bem-vindo ao time, {jogador}! Mostre seu talento!'

jogadores = [
    {'nome':'Neymar', 'status':'lesionado'},
    {'nome':'Gabigol', 'status':'titular'},
    {'nome':'Vinicios Jr', 'status':'reserva'},
    {'nome':'Ronaldo', 'status':'estrear'}
]
# print(painel_tatico(jogadores))

for numero in jogadores:
    jogador = numero['nome']
    status = numero['status']
    if numero['status'] == 'lesionado':
        print(painel_tatico(cuidar_lesionado,'💊', jogador))
    elif numero['status'] == 'titular':
        print(painel_tatico(motivar_jogador, '🔥', jogador))
    elif numero['status'] == 'estrear':
        print(painel_tatico(estreia_jogador, '🎉', jogador))
    elif numero['status'] == 'reserva':
        print(painel_tatico(preparar_para_reserva, '⚽', jogador))









