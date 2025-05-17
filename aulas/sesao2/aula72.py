# crie uma funçao que multiplique  todos os argumentos

# def soma(*args):
#     tot = 0
#     for numero in args:
#         vezes = numero
#         tot += numero * vezes
        
#     return tot

# total = soma(2,3,4)
# print(total)

# cria uma finção que fala se a função e par ou inpar

def jugar(*args):
    for numero in args:
        if numero % 2 == 0:
            print('Numero e Par')
        else:
            print('Numero e Impar')
resultado = jugar(3,4,5,6,7,8)


