def calcular(*args):
    total = 1
    for numero in args:
        total *= numero
    print(total)

total = calcular(1,2,3,4,5)