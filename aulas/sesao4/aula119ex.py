#Crie um programa similar que simula estratégias de jogo durante uma partida, com os seguintes comandos:
'''
estrategia: adiciona uma nova estratégia (ex: "marcação alta", "jogo de contra-ataque")

recuar: desfaz a última estratégia

avançar: refaz uma estratégia desfeita

ver_plano: mostra todas as estratégias atuais
'''

def plano(estartegias):
    if not estartegias :
        print('Não tem tarefas ainda')
        print('\n')
        return 
    print('\n')
    print()
    for i in estrategias:
        print(i)
    print('\n')
    
def recuar(estrategias,estrategia, refazer_estartegia):
    if not estrategias :
        print('Não tem nenhuma tarefa recuada')
        print('\n')
        return 
    estrategia = estrategias.pop()
    refazer_estartegia.append(estrategia)

def avancar(refazer_estartegia,estrategia,estrategias):
    if not refazer_estartegia :
        print('Não tem nenhuma tarefa para avançar')
        print('\n')
        return 
    estrategia = refazer_estartegia.pop()
    estrategias.append(estrategia)
    print()


def adicionar_estrategia(estrategia,estrategias):
    estrategia = estrategia.strip()
    estrategias.append(estrategia)
   


estrategias = []
refazer_estartegia = []
while True:
    print('comandos: estrategia, recuar e avançar, plano')
    estrategia = input('Digite um plano de jogo: ')

    if estrategia == 'plano':
        plano(estrategias)
        continue
    elif estrategia == 'recuar':
        recuar(estrategias,estrategia, refazer_estartegia)
        continue
    elif estrategia == 'avancar':
        avancar(refazer_estartegia,estrategia,estrategias)
        continue
    else:
        adicionar_estrategia(estrategia,estrategias)
        continue




