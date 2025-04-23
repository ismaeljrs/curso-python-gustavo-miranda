





# 🔹 4. Mapeamento de Dados em List Comprehension (map)

# Exercícios:
# 1️⃣ Use map() para dobrar os valores de uma lista [1, 2, 3, 4, 5].
lista = [1, 2, 3, 4, 5]

valor = list(map(lambda a : a * 2, lista))
print(valor)

# 2️⃣ Converta uma lista de números para string usando map() → Exemplo: [1, 2, 3] → ["1", "2", "3"].
lista1 = [1, 2, 3, 4, 5]

valor1 = list(map(lambda a : str(a), lista1))
print(valor1)

# 3️⃣ Resolva os exercícios acima usando list comprehension ao invés de map().

list2 = [str(i) for i in range(1,6)]
print(list2)