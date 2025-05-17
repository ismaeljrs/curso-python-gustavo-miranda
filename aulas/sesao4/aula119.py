#Execicios lista de tarefas  com desfazer e refazer 

#comando : listar , desfazer , refazer 
# lista_tarefas = []
# lista_refazer = []
# def mostrar_lista():
#     for numero, lista in enumerate(lista_tarefas):
#         print(f'{numero} {lista}')
# def refazer():
#     ...
# def desfazer():
#     lista.pop()

# while True:

#     digite = input('comando 1 - listar | 2- desfazer |3 - refazer: ')


#     if digite == '1':
#         mostrar_lista()
#     elif digite == '2':
#         if not lista_refazer:
#             print('não tem item ')
#         else:
#             mostrar_lista()
            
#     elif digite == '3':
#         ...
#     else:   
#         lista_tarefas.append(digite)


# ta to repetindo esse codigo varias vezes oq posso fz para parar de repetir pq assim eu preciso fz pra ter um codigo limpo . Programador nao repeti codigo e um mal abito.
import json

def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        print('\n')
        return 
    print('tarefas: ')
    for tarefa in tarefas:
        print(f'\t{tarefa}') # \t <- e um tab 
    print('\n')

def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefas para desfazer')
        print('\n')
        return 
    tarefa = tarefas.pop()
    tarefas_refazer.append(tarefa)
    print()

def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhua tarefas para refazer')
        print('\n')
        return 
    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)
    print()

def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip() #<- garantir que nao tenha espaço
    tarefas.append(tarefa)
    print()

tarefas = []
tarefas_refazer = []

while True: 
    print('Comando:lista, desfazer e refazer , finalizar ')
    tarefa = input('Digite uma tarefa ou comando: ')

    if tarefa == 'listar':
        listar(tarefas)
        continue
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        continue
    elif tarefa == 'refazer':
        refazer(tarefas,tarefas_refazer)
    elif tarefa == 'finalizar':
        finalizar = input('Deseja continuar? ').lower()
        if finalizar == 'n':
            add_txt = input('Deseja adicionar um arquivo no Json? s/n: ')
            if add_txt == 's':
                dados = []
                with open('tarefas.jason', 'w', encoding='utf-8') as arquivo:
                    json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)
                print('Tarefas Salvas com sucesso em tarefas.jason')
                
        break   
    else:   
        adicionar(tarefa, tarefas)
        continue

