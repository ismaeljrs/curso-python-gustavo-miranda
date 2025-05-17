#metodos de class 

# class Pessoa:
#     ano_atual = 2024
#     def __init__(self, nome, idade):
#         self.nome = nome 
#         self.idade = idade 
#     @classmethod # ele fz que chama a class sem passar self pra que usar ? -> 
#     def get_ano_nascimento(cls, idade):
#         return cls.ano_atual - idade 
# p1 = Pessoa('João', 19)

# print(p1.__dict__)#dict nao e so leitura
# print(p1.get_ano_nascimento(19))

class Produto:
    desconto = 0.10  # 10%

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self):
        self.preco -= self.preco * Produto.desconto

    @classmethod # entendi isso e bom usar so quando for passar sem expecifico  pass junto com class mae , e nao sua self 
    def mudar_desconto(cls, novo_desconto):
        cls.desconto = novo_desconto / 100  # Ex: 20 vira 0.20

    @staticmethod # esse nao depende do self e nem do cls 
    def eh_preco_valido(preco):
        return preco > 0

    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f}"
    
p1 = Produto("Mouse", 150) #
print(p1)  # Mouse - R$150.00
p1.aplicar_desconto()
print(p1)  # Mouse - R$135.00

Produto.mudar_desconto(20)  # Agora o desconto é de 20%
p2 = Produto("Teclado", 200)
p2.aplicar_desconto()
print(p2)  # Teclado - R$160.00

print(Produto.eh_preco_valido(0))   # False
print(Produto.eh_preco_valido(300)) # True
