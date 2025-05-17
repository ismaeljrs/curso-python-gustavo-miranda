
# matriz = [
#     [0,0,0],
#     [0,0,0],
#     [0,0,0]
# ]

# for i in range(0,3):
#     for l in range(0,3):
#         matriz[i][l] = input(f'Digite {[i]}{[l]}: ')
    
# for i in range(0,3):
#     for l in range(0,3):
#         print(f'{matriz[i][l]:^5}', end='')
#     print()

"""
numero_1 = 0.1
numero_2 = 0.2
numero_3 = numero_1 + numero_2

print(numero_3)
print(f'{numero_3:.1f}')

"""
# split()
frase = '   Ola meu nome e    ,    ismael como vc estar?      '
letras_frases = frase.split(',') #pode usar para separa so na virgula 
print(letras_frases)

#strip()  # corta o espaço no começo e no fim
corigido = []

for i ,frases in enumerate(letras_frases):
    corigido.append(letras_frases[i].strip())

print(corigido)


frases_unidas = '-'.join(corigido)
print(frases_unidas)



