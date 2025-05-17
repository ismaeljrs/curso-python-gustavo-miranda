'''
1️⃣ Crie uma função lambda que receba um número e retorne seu dobro.
2️⃣ Escreva uma função lambda que receba dois números e retorne o maior deles.
3️⃣ Crie uma função lambda que receba um nome e retorne ele em maiúsculas.

'''
#1️⃣
soma = lambda x: x * 2
print(soma(3))

#2️⃣

soma_2 = lambda x ,y: x if x > y else y if x < y else 'empate'

print(soma_2(3,7))

#3️⃣
nome = str(input('Qual é o seu nome?: '))

nome_maiuscula = lambda nome: nome.upper()
print(nome_maiuscula(nome))

