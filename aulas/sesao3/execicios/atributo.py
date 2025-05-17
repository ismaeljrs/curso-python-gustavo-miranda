#atributo

# class Treinador:
#     inicio_carreira = 2000

#     def __init__(self,nome,ano):
#         self.nome = nome
#         self.ano = ano
    
#     def anos_de_experiencia(self):
#         return self.ano - Treinador.inicio_carreira 

# t1 = Treinador('neymar',2025)

# print(f'{t1.nome} tem {t1.anos_de_experiencia()} anos de experiencia')

#atributo
class Pessoa:
    ano_atual = 2025

    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade 

    def Ex_ano_de_idade(self):
        return Pessoa.ano_atual - self.idade
    
    def experincia_de_vida(self):
        return Pessoa.ano_atual - self.idade

nome = str(input('Qaul e o seu nome?: '))  
idade = int(input('Voce tem quantos anos?: '))
pessoa = Pessoa(nome,idade)

print(pessoa.__dict__)



