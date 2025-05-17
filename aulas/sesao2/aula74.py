def contador():
    total = 0  # Variável "privada"

    def incrementar():
        nonlocal total
        total += 1
        return total

    return incrementar

contar = contador()
print(contar())  # 1
print(contar())  # 2
