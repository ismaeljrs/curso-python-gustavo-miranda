

caminho_arquivo = 'c:/Users/ismae/OneDrive/Documentos/CursoPythonMiranda/curso-python-gustavo-miranda/aulas/jason/aula117.py'
caminho_arquivo += 'aula117.txt'

# arquivo = open(caminho_arquivo, 'w')

# arquivo.close()
with open ( caminho_arquivo, 'a' ) as arquivo: # a vai continuar aonde parou 
    arquivo.write('linha 2\n')
