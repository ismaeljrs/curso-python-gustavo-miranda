import json

class Jogador:
    ano_atual = 2025
    def __init__(self, nome, idade , cpf=None):
        self.nome = nome
        self.idade = idade 
        self.cpf = cpf
    def Ano_de_nascimento(self):
        return Jogador.ano_atual - self.idade
    
j1 = Jogador('ismael', 19)
print(f'Idade {j1.Ano_de_nascimento()}')
print(j1.__dict__)

with open('caminho.json','w',encoding='utf-8') as arquivo:
    json.dump(j1.__dict__, arquivo, ensure_ascii=False, indent=4)
print('Salvo no arquivo "caminho.json"')
