# class Escritor:
#     def __init__(self , nome) -> None:
#         self.nome = nome
#         self._ferramenta = None
    
#     @property
#     def ferramenta(self):
#         return self._ferramenta
    
#     @ferramenta.setter
#     def ferramenta(self, ferramenta):
#         self._ferramenta = ferramenta

# class FerramentaDeEscrever :
#     def __init__(self, nome):
#         self.nome = nome

#     def escrever(self):
#         return f'{self.nome} esta escrevendo'

# escritor = Escritor('luiz')
# caneta = FerramentaDeEscrever('caneta bic')
# escritor.ferramenta = caneta

# print(caneta.escrever())
# print(escritor.ferramenta.escrever())

#execicio 1 facil

# AGREGAÇÃO DE ORIENTACAO A OBJETOS 
# CADA OBJETO TEM SEU CICLI DE VIDA NEM DOS DOIS DEPENDE OD OUTRO 

#--------> AULA
# class Carrinho: 
#     def __init__(self): # base de dados que vai salavr os produtos 
#         self._produtos = []

#     def total(self):
#         return sum([p.preco for p in self._produtos])
    
#     def inserir_produtos(self, *produtos):
#         self._produtos.extend(produtos) #append so resebe um objeto mais axpend cresce um os elementos da outra 

#     def lista_produtos(self):
#         print()
#         for produto in self._produtos:
#             print(produto.nome, produto.preco)
#         print()

# class Produto:
#     def __init__(self, nome , preco):
#         self.nome = nome
#         self.preco = preco

# carrinho = Carrinho()
# p1, p2 = Produto('Caneta', 1.20), Produto('Camiseta', 20) 
# carrinho.inserir_produtos(p1,p2)
# carrinho.lista_produtos()


# ---------> Atividade

class Livro:
    def __init__(self, titulo , autor, preco ):
        self.titulo = titulo
        self.autor = autor
        self.preco = preco


class Biblioteca:
    def __init__(self):
        self._livros = []


    def adicionar_livros(self, *livros):
        self._livros.extend(livros)
        print('adicionou')

    def mostrar_livros(self):
        for items in self._livros:
            print(f'{items.titulo} , {items.autor} , {items.preco}')


    
biblioteca = Biblioteca()
autor = Livro('Caxinhos dorados', 'Ismael', 19)
biblioteca.adicionar_livros(autor)
biblioteca.mostrar_livros()















