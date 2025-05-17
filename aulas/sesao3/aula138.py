#herança 

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def fala_nome_classe(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Cleinte(Pessoa):
    ...

class Aluno(Pessoa):
    cpf = 'cpf Aluno'

c1 = Cleinte('Luiz', 'Otavio')
c1.fala_nome_classe()
a1 = Aluno('Maria', 'Helena')
a1.fala_nome_classe()
print(a1.cpf)

#herança deixa o codigo extremamente complexo para debugar 
#uso com moderação iniciante

