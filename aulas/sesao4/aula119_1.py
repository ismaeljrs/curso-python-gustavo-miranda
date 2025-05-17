# Fz que o codigo não se repita muito, tentar fazer o maximo
#como evitar uso de if

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
    print('Comando:lista, desfazer e refazer ')
    tarefa = input('Digite uma tarefa ou comando: ')

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda:  refazer(tarefas, tarefas_refazer),
        'adicionar': lambda: adicionar(tarefa, tarefas),
    }
    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
        comandos['adicionar']
    comando()
    # get() é usado com dicionários  Acessar o valor de uma chave de forma segura




