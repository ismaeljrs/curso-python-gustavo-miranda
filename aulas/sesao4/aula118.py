#problema dos parametros mutaveis no python

def adicionar_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = adicionar_clientes('luiz')
print(cliente1)
adicionar_clientes('fernando',cliente1)
adicionar_clientes('nycole',cliente1)
print(cliente1)


