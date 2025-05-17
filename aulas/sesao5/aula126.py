#__dict__ atributo e instancia

class Pessoa:
    ano_atual = 2024
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade 

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
p1 = Pessoa('João', 19)

print(p1.__dict__)#dict nao e so leitura
print(p1.get_ano_nascimento())