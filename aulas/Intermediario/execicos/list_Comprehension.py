




# 1️⃣ Crie uma lista de quadrados dos números de 1 a 10 usando list comprehension.
quadrado = [x for x in range(10+1)]
print(quadrado)


# 2️⃣ Gere uma lista apenas com os números pares de 1 a 20.


lista_pares = [x for x in range(20) if x % 2 == 0]
print(lista_pares)


# 3️⃣ Construa uma lista de strings com "Número X" onde X varia de 1 a 5 (["Número 1", "Número 2", ...]).

nuemro = [f'Número {i}' for i in range(1,6)]
print(nuemro)