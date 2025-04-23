import json

aluno = []


try:
    for i in range(2):
        Nome_alunos = {}
        nome = str(input('nome: '))
        Nome_alunos['nome'] = nome
        media = []

        for j in range(4):
            nota = float(input('Nota: '))
            media.append(nota)
        Nome_alunos['media'] = sum(media) / 4
        aluno.append(Nome_alunos)
except ValueError:
    print('Digite apenas números ')
    
for numero,i in enumerate(aluno, start=1):
    for k,v in i.items():
        print(f'Aluno {numero}')
        print(f'{k} =  {v}')
        print('\n')

for i, dados in enumerate(aluno, start=1):
    if dados['media'] >= 6:
        print(f"{dados['nome']} está aprovado")
    else:
        print(f"{dados['nome']} está reprovado")

with open( 'nota.jason', 'w',encoding='utf8') as arquivo:
    json.dump(aluno, arquivo,indent=2)

# opcao = input('Deseja criar uma lista (s/n)').lower()

# if opcao == 's':
#     notas_arquivo = 'notas_alunos.txt'
#     with open( notas_arquivo, 'w') as arquivo:
#         for dados in aluno:
#             situacao = 'aprovado' if dados['media'] >= 6 else 'Reprovado'
#             arquivo.write(f'Nome: {dados['nome']}, Média: {dados['media']:.2f}, {situacao}\n')
#         print(f'Arquivo {notas_arquivo} criado com sucesso', )




        



    
        





