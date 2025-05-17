







# 🔹 5. List Comprehension com Mais de um for

# Exercícios:
# 1️⃣ Gere todas as combinações possíveis entre duas listas [1, 2] e ["A", "B"].

lista1 = [1, 2]
lista2 = ["A", "B"]

juntos = [(x,y) for x in lista1 for y in lista2]
print(juntos)

# lista = [
#     (x,y) for y in 'ABCDE'
#     for x in range(3)
# ]
# print(lista)

# 2️⃣ Crie uma lista com os produtos de cada número de [1, 2, 3] multiplicado por cada número de [4, 5, 6].
# 3️⃣ Construa uma lista com tuplas de (x, y, x*y), onde x vai de 1 a 3 e y de 1 a 3.